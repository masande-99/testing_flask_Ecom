from flask import request

from tests.base_test import BaseTest
from market import db
from market.models import User


class TestRegister(BaseTest):
    def test_register_new_user(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                # Asserting that the user is found in the database
                self.assertTrue(user)

                # asserting that the user is shown the message below
                self.assertIn(b'Account created successfully! You are now logged in as', response.data)

                # Asserting that the user is redirected to the market page
                self.assertEqual('http://localhost/market', request.url)


