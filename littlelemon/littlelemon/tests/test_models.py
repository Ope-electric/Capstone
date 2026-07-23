from django.test import TestCase

from .models import MenuItem

class MenuTestCase(TestCase):
    def test_get_item(self):
        menu_item = MenuItem.objects.create(
            title='Test Item',
            price=9.99,
            inventory=10
        )
        expected_output = 'Test Item : 9.99'
        self.assertEqual(menu_item.get_item(), expected_output)

    def test_get_item(self):
        expected_output = 'Test Item : 9.99'
        self.assertEqual(self.menu_item.get_item(), expected_output)