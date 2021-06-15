from flask import request

from tests.base_test import BaseTest
from market import db
from market.models import User, Item


class TestMarketRoute(BaseTest):
    def test_market_route(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()
                self.assertTrue(user)

                respons = self.app.post('/login', data=dict(username="JoeDoe", password="202177"), follow_redirects=True)

                self.assertIn(b'Success! You are logged in as: JoeDoe', respons.data)

                # Asserting that the user is redirected to the market page after login
                self.assertEqual('http://localhost/market', request.url)

                purchased_item = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket", owner=1).buy(user).get_data()

                self.assertFalse(purchased_item)

                purchase_item = self.app.post('/market', follow_redirects=True).get_data()

                self.assertTrue(purchase_item)
                self.assertIn(b'Congratulations! You purchased', purchased_item)
