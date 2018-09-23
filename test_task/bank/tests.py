import json
from django.test import TestCase, Client
from django.urls import reverse
from .models import Banknote


class BankViewTests(TestCase):

    def setUp(self):
        # PostRate.objects.create(**KWARGS)
        self.client = Client()
        Banknote.objects.create(denominator=5, quantity=6)
        Banknote.objects.create(denominator=2, quantity=8)

    def test_bank_set_for_negative_values(self):
        url = reverse('bank_set')
        data = {
            "10": -2,
            "5": 1
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_bank_set_for_not_int(self):
        url = reverse('bank_set')
        data = {
            "1xc": -2,
            "5": 1
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_bank_set_view(self):
        url = reverse('bank_set')
        data = {
            "10": 5,
            "5": 4
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_algorithm_withdraw(self):
        url = reverse('withdraw')
        data = {
            "amount": 21
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        if response.status_code==200:
            notes = json.loads(response.content)
            sum = 0
            for key in notes.keys():
                sum += int(key)*notes[key]

            self.assertEqual(sum, data["amount"])

