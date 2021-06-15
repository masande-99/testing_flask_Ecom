from flask import request

from tests.base_test import BaseTest
from market import db
from market.models import User
from market.forms import RegisterForm


class TestForms(BaseTest):
    def test_username_already_exist(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                response = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user1 = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                exists = RegisterForm.validate_username(self, username_to_check=user1)


