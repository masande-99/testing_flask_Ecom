from tests.base_test import BaseTest
from market import db
from market.models import User, Item


class TestCanSell(BaseTest):
    def test_market_password_correction(self):
        with self.app:
            with self.app_context:
                # Registering a new user
                response = self.app.post('/register',
                                         data=dict(id=1, username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user1 = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                # Logging in with a correct password
                password_hash = User.check_password_correction(user1, "202177")
                self.assertTrue(password_hash)

                # Logging in with an incorrect password
                password_hash1 = User.check_password_correction(user1, "202176")
                self.assertFalse(password_hash1)

    def test_password_method(self):
        with self.app:
            with self.app_context:
                # Registering a new user
                response = self.app.post('/register',
                                         data=dict(id=1, username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user1 = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                # Logging in with a correct password
                password_hash = user1.password
                self.assertTrue(password_hash)

    def test_password_setter_method(self):
        with self.app:
            with self.app_context:
                # Registering a new user
                response = self.app.post('/register',
                                         data=dict(id=1, username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user1 = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                self.assertNotEqual(user1.password_hash, "202177")
