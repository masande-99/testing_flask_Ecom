from tests.base_test import BaseTest
from market import db
from market.models import User, Item


class TestSellBuy(BaseTest):
    def test_buy_method(self):
        with self.app:
            with self.app_context:
                # Registering a new user
                response = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)
                user1 = db.session.query(User).filter_by(email_address="joe@gmail.com").first()
                self.assertTrue(user1)

                item = Item(name="New Product", price=200, barcode=1234567, description="This is a jacket")
                db.session.add(item)
                db.session.commit()

                a = db.session.query(Item).filter_by(name="New Product")
                self.assertTrue(a)

                buy = item.buy(user1)
                self.assertEqual(user1.budget, 800)
                self.assertEqual(item.owner, 1)

                sell = item.sell(user1)
                self.assertEqual(user1.budget, 1000)
                self.assertEqual(item.owner, None)
