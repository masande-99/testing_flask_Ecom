from market.models import Item
from unittest import TestCase


class TestItem(TestCase):
    def test_create_item(self):
        item = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket")

        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, "New Product")
        self.assertEqual(item.price, 200)
        self.assertEqual(item.barcode, 1234567)
        self.assertEqual(item.description, "This is a jacket")
