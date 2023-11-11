from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class TestProfileViews(TestCase):
    """
    Testing Profile Views
    """

    def setUp(self):
        """
        Setup creates user, profile and logs user in
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@test.com", password="testpass"
        )
        self.profile = Profile.objects.get(user=self.user)
        self.client.login(username="testuser", password="testpass")

    def test_profile_page_renders(self):
        """
        Test that profile view renders correct page
        """
        response = self.client.get(reverse("profile", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

