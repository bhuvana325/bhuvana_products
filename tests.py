from django.test import TestCase
from .models import items


# Create your tests here.


# Create your tests here.
class Basictests(TestCase):
    def setup(self):
        items.objects.create(name='Lenovo',
                             cost_per_item=40000,
                             stock_quantity=40,
                             volume=1600000)

    def test_get_method(self):
        url = "http://127.0.0.1:8000/products/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        qs = items.objects.filter(name='Lenovo')
        self.assertEqual(qs.count(), 0)
