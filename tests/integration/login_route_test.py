from flask import request

from tests.base_test import BaseTest
from market import db
from market.models import User

class TestLogin(BaseTest):
    def test_login_successful(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()
                self.assertTrue(user)

                respons = self.app.post('/login', data=dict(username="JoeDoe", password="202177"), follow_redirects=True)

                self.assertIn(b'Success! You are logged in as:', respons.data)

                # Asserting that the user is redirected to the market page after login
                self.assertEqual('http://localhost/market', request.url)


    def test_login_not_successful(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                self.assertTrue(response.status_code, 200)

                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()
                self.assertTrue(user)

                respons = self.app.post('/login', data=dict(username="JoeDo", password="202177"), follow_redirects=True)

                self.assertIn(b'Username and password are not match! Please try again', respons.data)

                # Asserting that the user is redirected to the login page after submitting
                self.assertEqual('http://localhost/login', request.url)

