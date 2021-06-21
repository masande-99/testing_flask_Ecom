from market.models import Item
from unittest import TestCase


class TestReprMethod(TestCase):
    def test_repr_method(self):
        item = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket")
        repr_ = item.__repr__()

        self.assertTrue(item)
        self.assertIn('New Product', repr_)
