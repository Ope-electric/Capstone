from django.test import TestCase
from .models import MenuItem
class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item = MenuItem.objects.create(
            title='Test Item',
            price=9.99,
            inventory=10
        )
        
    def test_get_item(self):
        expected_output = 'Test Item : 9.99'
        self.assertEqual(self.menu_item.get_item(), expected_output)
        
    