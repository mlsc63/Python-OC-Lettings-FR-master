from django.test import TestCase
from .models import Letting
from django.contrib.auth.models import User
from app.models import Address
from django.urls import reverse


class TestLetting(TestCase):
    def setUp(self):
        self.address = Address.objects.create(number=105,
                                              street="boulevard desaix", city="riom", state="test",
                                              zip_code=63200, country_iso_code="")
        self.letting = Letting.objects.create(title="test titre", address=self.address)
        self.reverse = reverse('lettings:lettings_index')

    def test_animals_can_speak(self):
        response = self.client.get(self.reverse)
        self.assertContains(response, text='test titre')
