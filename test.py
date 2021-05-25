from werkzeug.wrappers import response
from run import app

from socialtracking.users.routes import hash_password
from socialtracking.users.forms import LoginForm
import unittest
from unittest.mock import Mock

class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Corona Virus Impact Reduction App' in response.data)
        self.assertTrue(b'The Project' in response.data)
        self.assertTrue(b'Username' in response.data)


    def test_register_page(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertTrue(b'Register' in response.data)
        self.assertTrue(b'Confirm Password' in response.data)
        self.assertTrue(b'Already have an account' in response.data)

    def test_home_page(self):
        tester = app.test_client(self)
        response = tester.get('/homepage', content_type='html/text')
        self.assertTrue(b'You should be redirected automatically' in response.data)

    def test_hash_password(self):
        mock = Mock()
        mock.password.data = '123'
        self.assertNotEqual("123", hash_password(mock))
        self.assertEqual("$", hash_password(mock)[0])
        self.assertEqual("$", hash_password(mock)[3])

if __name__ == '__main__':
    unittest.main()