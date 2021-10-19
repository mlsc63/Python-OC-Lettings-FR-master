from django.test import TestCase
from .models import Profile
from django.urls import reverse
from django.contrib.auth.models import User


class TestLetting(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test')
        self.profile = Profile.objects.create(user=self.user, favorite_city="Riom")

        self.reverse = reverse("profile:profiles_index")

        self.reverse_id = reverse("profile:profile", args=['test'])

    def test_profile(self):
        response = self.client.get(self.reverse)
        self.assertContains(response, text='test')

    def test_profile_id(self):
        response = self.client.get(self.reverse_id)
        self.assertContains(response, text='test')
