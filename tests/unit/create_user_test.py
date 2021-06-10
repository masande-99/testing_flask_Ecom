from market.models import User
from unittest import TestCase


class TestUser(TestCase):
    def test_create_user(self):
        user = User(id=1, username="joe", email_address="joe@gmail.com", password_hash="Joee", budget=1000)

        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, "joe")
        self.assertEqual(user.email_address, "joe@gmail.com")
        self.assertEqual(user.password_hash, "Joee")
        self.assertEqual(user.budget, 1000)


