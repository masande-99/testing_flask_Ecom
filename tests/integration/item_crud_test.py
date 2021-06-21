from market.models import Item
from tests.base_test import BaseTest
from market import db


class TestItemCrud(BaseTest):
    def test_item_crud(self):
        item = Item(name="New Product", price=200, barcode=1234567, description="This is a jacket")

        db.session.add(item)
        db.session.commit()

        availaible = db.session.query(Item).filter_by(name="New Product").first()
        # Asserting that the item is available in the database
        self.assertTrue(availaible)

        db.session.delete(item)
        db.session.commit()
        not_available = db.session.query(Item).filter_by(name="New Product").first()
        # Asserting that the item is not found in the database
        self.assertIsNone(not_available)

