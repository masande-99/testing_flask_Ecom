from flask import request

from tests.base_test import BaseTest
from market import db
from market.models import User, Item


class TestCanSell(BaseTest):
    def test_can_sell_item(self):
        with self.app:
            with self.app_context:
                # Registering a new user
                response = self.app.post('/register',
                                         data=dict(id=1, username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user1 = db.session.query(User).filter_by(email_address="joe@gmail.com").first()
                # Asserting that user is found in the database
                self.assertTrue(user1)

                res = self.app.post('/register',
                                    data=dict(id=2, username="JoDoe", email_address="jo@gmail.com",
                                              password1="202176", password2="202176",), follow_redirects=True)

                user2 = db.session.query(User).filter_by(email_address="jo@gmail.com").first()
                # Asserting that the user is found in database
                self.assertTrue(user2)

                # Creating a new item object
                item = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket", owner=1)
                db.session.add(item)
                db.session.commit()

                # checking that the item is found in the database
                product = db.session.query(Item).filter_by(name="New Product")

                # Asserting that the product is available in the database
                self.assertTrue(product)

                # Asserting that the user1 can buy the product
                self.assertTrue(user1.can_sell(item_obj=item))

                # Asserting that user2 cannot buy the product
                self.assertFalse(user2.can_sell(item_obj=item))


