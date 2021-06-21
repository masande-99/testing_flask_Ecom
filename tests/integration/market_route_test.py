from flask import request

from tests.base_test import BaseTest
from market import db
from market.models import User, Item


class TestMarketRoute(BaseTest):
    def test_market_route_can_purchase(self):
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

                # no need for a post request because the user is redirected to the market route automatically
                market_post_request = self.app.post('/market', follow_redirects=True)
                self.assertTrue(market_post_request.status_code, 200)

                purchased_item = Item(id=1, name="New Product", price=200, barcode=1234567,
                                      description="This is a jacket")

                purchased_item1 = Item(id=1, name="New Product", price=2000, barcode=1234567,
                                       description="This is a jacket")

                self.assertTrue(user.can_purchase(purchased_item))
                self.assertFalse(user.can_purchase(purchased_item1))

    def test_market_route_can_sell(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(id=1, username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()
                self.assertTrue(user)

                response1 = self.app.post('/register',
                                          data=dict(id=2, username="JoDoe", email_address="jo@gmail.com",
                                                    password1="202176", password2="202176",), follow_redirects=True)

                user1 = db.session.query(User).filter_by(email_address="jo@gmail.com").first()
                self.assertTrue(user1)

                # Asserting that the user is redirected to the market page after login
                self.assertEqual('http://localhost/market', request.url)

                # no need for a post request because the user is redirected to the market route automatically
                # market_post_request = self.app.post('/market', follow_redirects=True)
                # self.assertTrue(market_post_request.status_code, 200)

                purchased_item = Item(id=1, name="New Product", price=200, barcode=1234567,
                                      description="This is a jacket", owner=1)
                db.session.add(purchased_item)
                db.session.commit()

                self.assertTrue(user.can_sell(purchased_item))
                self.assertFalse(user1.can_sell(purchased_item))

    def test_market_route_returns_market(self):
        with self.app:
            with self.app_context:
                response1 = self.app.post('/register',
                                          data=dict(id=2, username="JoDoe", email_address="jo@gmail.com",
                                                    password1="202176", password2="202176",), follow_redirects=True)

                response = self.app.post('/market', follow_redirects=True)

                self.assertEqual('http://localhost/market', request.url)
