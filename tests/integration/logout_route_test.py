from flask import request

from tests.base_test import BaseTest
from market import db
from market.models import User


class TestLogout(BaseTest):
    def test_user_logged_out_successfully(self):
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

                # Logging the user out
                res = self.app.post('/logout', follow_redirects=True)

                # Asserting that the user is redirected to the logged out page
                self.assertEqual('http://localhost/logout', request.url)


    def test_logout_route_returns_home_page(self):
        with self.app:
            with self.app_context:
                request = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()
                self.assertTrue(user)


                request1 = self.app.post('/logout', follow_redirects=True)

                self.assertEqual(200, request1.status_code)
                self.assertEqual('http://localhost/logout', request.url)


