""" tests.py """
from app import app
from app.models import User
# import unit test
import unittest
import json

class BaseTestCase(unittest.TestCase):
    def createapp_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        """Define test variables and initialize app."""
        tester = app.test_client(self)
        self.user = {
            "id": "1",
            "firstname": "christine",
            "lastname": "nakyobe",
            "username": "christine",
            "email": "xtine@gmail.com",
            "password": "abcd",
            "gender": "female"
        }   

        self.login = {
            'id': '1',
            'username':'frank',
            'password':'abcd'
        }

        self.business = {
            'id':'1',
            'businessname':'Kagz',
            'location': 'Kampala',
            'category':'electronics',
            'email':'kagz@gmail.com',
            'address':'P.O.Box 2334',
            'phonenumber':'0704895678'
        }

        self.reviews = {
            'id':'1'
            'reviews': ''
        }
class UserTestCase(BaseTestCase):
    """This class represents the users test case """
        
    def test_API_create_User(self):
        """Test API can create a User (POST request)"""
        tester = app.test_client(self)
        res = tester.post('/api/auth/register', data= json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        self.assertIn("female", str(res.data))

    def test_API_user_login(self):
        """Test API can login(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/auth/login', data= json.dumps(self.login))
        self.assertEqual(res.status_code, 201)
        self.assertIn("female", str(res.data))

    def test_API_user_logout(self):
        """Test API can logout(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/auth/login', data= json.dumps(self.login))
        self.assertEqual(res.status_code, 201)
        self.assertIn("frank", str(res.data))

    def test_can_create_business(self):
        """Test API can create Business(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/auth/register', data= json.dumps(self.business))
        self.assertEqual(res.status_code, 201)
        self.assertIn("Kagz", str(res.data))

    def test_can_update_business(self):
        """Test API can create Business(POST request) """
        tester = app.test_client(self)
        res = tester.put('/api/auth/businesses/businessid', data= json.dumps(self.business))
        self.assertEqual(res.status_code, 201)
        self.assertIn("Kagz", str(res.data))

    def test_password_reset(self):
        """Test API can create Business(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/auth/reset-password', data= json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        self.assertIn("Kagz", str(res.data))

if __name__ == '__main__':
    unittest.main()