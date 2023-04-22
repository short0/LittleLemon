from django.test import TestCase
from restaurant.models import Menu
from django.core import serializers

class MenuViewTest(TestCase):
    def setup(self):
        self.client = Client()
        Menu.objects.create(title='IceCream', price=80, inventory=100)
        Menu.objects.create(title='IceCream2', price=82, inventory=102)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        expected = serializers.serialize('json', Menu.objects.all())
        self.assertJSONEqual(response.content, expected)
