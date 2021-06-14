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

                # Checking that the user has a budget of 1000
                budget = db.session.query(User).filter_by(budget=1000).first()

                # Asserting that the user has a budget of 1000
                self.assertTrue(budget)

                # asserting that the user is shown the message below
                self.assertIn(b'Account created successfully! You are now logged in as JoeDoe', response.data)

                # Asserting that the user is redirected to the market page
                self.assertEqual('http://localhost/market', request.url)

    def test_password_dont_match(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="20217", ), follow_redirects=True)

                # checking if the user is not in the User table
                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                # Asserting that the user is found in the database
                self.assertFalse(user)

                # Asserting that the user was shown an error message
                self.assertIn(b'There was an error with creating a user: '
                              b'[&#39;Field must be equal to password1.&#39;]', response.data)

    def test_user_exists(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register', data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                                password1=7887476, password2=7887476), follow_redirects=True)

                # checking if the user is  in the User table
                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                # Asserting that the user is found in the database
                self.assertTrue(user)

                respons = self.app.post('/register', data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                                password1=7887476, password2=7887476), follow_redirects=True)

                # checking if the user is  in the User table
                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                # Asserting that the user is found in the database

                self.assertTrue(user)

                # Asserting that the user is shown this error message
                self.assertIn(b'There was an error with creating a user: [&#39;Username '
                              b'already exists! Please try a different username&#39;]', respons.data)



