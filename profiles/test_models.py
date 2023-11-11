from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class TestProfileModel(TestCase):
    def setUp(self):
        """
        Sets up a User and associated Profile for testing.
        """
        self.user = User.objects.create_user(
            username="testuser", email="testuser@test.com", password="testpass"
        )
        self.profile = Profile.objects.get(user=self.user)
        self.profile.bio = "This is a test bio."
        self.profile.age = 30
        self.profile.weight = 70
        self.profile.save()

    def test_profile_model(self):
        """
        Tests the Profile model's attributes and methods.
        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.bio, "This is a test bio.")
        self.assertEqual(self.profile.age, 30)
        self.assertEqual(self.profile.weight, 70)
        # Add more assertions as necessary

    def test_profile_creation_on_user_creation(self):
        """
        Tests if a Profile is automatically created when a User is created.
        """
        new_user = User.objects.create_user(
            username="newtestuser", email="newtestuser@test.com", password="newtestpass"
        )
        new_profile = Profile.objects.get(user=new_user)
        self.assertIsNotNone(new_profile)
        # Add more assertions to check default values or other conditions
