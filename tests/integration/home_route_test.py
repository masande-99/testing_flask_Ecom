from flask import request

from tests.base_test import BaseTest


class TestHomeRoute(BaseTest):
    def test_home(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/home', follow_redirects=True)

                self.assertEqual('http://localhost/home', request.url)
                self.assertIn(b'Start purchasing products by clicking the link below', response.data)
                self.assertTrue(response.status_code, 200)

    def test_route(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/', follow_redirects=True)

                self.assertEqual('http://localhost/', request.url)
                self.assertIn(b'Start purchasing products by clicking the link below', response.data)



