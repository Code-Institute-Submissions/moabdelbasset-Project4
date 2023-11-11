from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from tracker.models import Tracker
from datetime import date

class TrackerViewTestCase(TestCase):
    def setUp(self):
        # Create a user and profile
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.profile, created = Profile.objects.get_or_create(user=self.user)
        self.client.force_login(self.user)

        # Create a Tracker instance
        self.tracker = Tracker.objects.create(
            user=self.profile,
            title='Chicken',
            date=date.today(),
            portion_size='250g',
            meal_type='Lunch',
            calories=350
        )

    def test_trackers_list_view(self):
        response = self.client.get(reverse('trackers'))  # replace 'trackers_url_name' with the actual url name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chicken')

    def test_add_tracker_view(self):
        response = self.client.post(reverse('add_tracker'), data={
            'title': 'Sushi',
            'date': date.today(),
            'portion_size': '300g',
            'meal_type': 'Dinner',
            'calories': 400
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertEqual(Tracker.objects.count(), 2)

    def test_edit_tracker_view(self):
        response = self.client.post(reverse('edit_tracker', args=[self.tracker.id]), data={
            'title': 'Meat',
            'date': date.today(),
            'portion_size': '250g',
            'meal_type': 'Lunch',
            'calories': 350
        })
        self.assertEqual(response.status_code, 302)
        self.tracker.refresh_from_db()
        self.assertEqual(self.tracker.title, 'Meat')


    def tearDown(self):
        # Cleanup any created data
        self.user.delete()
        self.tracker.delete()
