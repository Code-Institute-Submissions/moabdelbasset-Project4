from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from tracker.models import Tracker
from datetime import date

class TrackerModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@test.com', password='testpass')
        self.profile, created = Profile.objects.get_or_create(user=self.user)

        # Create a Tracker instance
        self.tracker = Tracker.objects.create(
            user=self.profile,
            title='Healthy Salad',
            date=date.today(),
            portion_size='250g',
            meal_type='Lunch',
            calories=350
        )

    def test_field_content(self):
        """Test the content of each field in Tracker model"""
        self.assertEqual(self.tracker.user, self.profile)
        self.assertEqual(self.tracker.title, 'Healthy Salad')
        self.assertEqual(self.tracker.date, date.today())
        self.assertEqual(self.tracker.portion_size, '250g')
        self.assertEqual(self.tracker.meal_type, 'Lunch')
        self.assertEqual(self.tracker.calories, 350)

    def test_tracker_str_representation(self):
        """Test the string representation of a Tracker instance"""
        self.assertEqual(str(self.tracker), f'Healthy Salad ({date.today()})')

    def test_meal_choices(self):
        """Test the meal choices for meal_type field"""
        meal_choices = dict(self.tracker.MEAL_CHOICES)
        self.assertIn(self.tracker.meal_type, meal_choices)

    def test_calories_value_on_save(self):
        """Test the calories value is set on save"""
        # Assuming the fetch_calories method sets a default value if not provided
        new_tracker = Tracker.objects.create(
            user=self.profile,
            title='Fruit Smoothie',
            date=date.today(),
            portion_size='200ml',
            meal_type='Snack'
        )
        self.assertNotEqual(new_tracker.calories, 0)

    def tearDown(self):
        # Cleanup any created data
        self.user.delete()
        self.tracker.delete()
