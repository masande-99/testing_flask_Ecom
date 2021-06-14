from market.models import Item, User
from tests.base_test import BaseTest


class TestItem(BaseTest):
    def test_create_item(self):
        item = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket")

        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, "New Product")
        self.assertEqual(item.price, 200)
        self.assertEqual(item.barcode, 1234567)
        self.assertEqual(item.description, "This is a jacket")

    def test_can_buy(self):

        item = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket", owner=1)

        user = User(id=1, username="joe", email_address="joe@gmail.com", password_hash="Joee", budget=1000).can_purchase(item)

        self.assertTrue(user)

    def test_can_sell_item(self):

        user = User(id=1, username="joe", email_address="joe@gmail.com", password_hash="Joee", budget=1000,)
        items = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket", owner=1).sell(user)

        # Asserting that there is no Item in items
        self.assertFalse(items)

    def test_budget_prettier(self):

        user = User(id=1, username="joe", email_address="joe@gmail.com", password_hash="Joee", budget=1000)

        self.assertTrue(user.prettier_budget, 1000)












