from market.models import Item, User
from unittest import TestCase


class TestItem(TestCase):
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

    def test_budget_prettier_returns_no_commar_if_int_len_is_less_than_4(self):

        user = User(id=1, username="joe", email_address="joe@gmail.com", password_hash="Joee", budget=800)

        self.assertNotEqual(user.prettier_budget, "1,000")

    def test_budget_prettier_returns_a_commar_if_int_len_is_equal_to_4(self):

        user = User(id=1, username="joe", email_address="joe@gmail.com", password_hash="Joee", budget=1000)

        self.assertEqual(user.prettier_budget, "1,000$")


    def test_can_not_buy(self):

        item = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket", owner=1)

        user = User(id=1, username="joe", email_address="joe@gmail.com", password_hash="Joee", budget=100).can_purchase(item)

        self.assertFalse(user)

