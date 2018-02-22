""" tests.py """
from app import app
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
            'username':'david',
            'password':'abcd123'
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
            'id':'1',
            'reviews': 'hello'
        }
class UserTestCase(BaseTestCase):
    """This class represents the users test case """
        
    def test_API_create_User(self):
        """Test API can create a User (POST request)"""
        tester = app.test_client(self)
        res = tester.post('/api/auth/register', data= json.dumps(self.user), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("user successfully added", str(res.data))

    def test_API_user_login(self):
        """Test API can login User (POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/auth/login', data= json.dumps(self.login), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("successfully logged in", str(res.data))

    def test_API_user_logout(self):
        """Test API can logout(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/auth/logout', data= json.dumps(self.login), content_type='application/json' )
        # self.assertEqual(res.status_code, 403)
        self.assertIn("false", str(res.data))

    def test_can_create_business(self):
        """Test API can create Business(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/businesses', data= json.dumps(self.business), content_type='application/json' )
        self.assertEqual(res.status_code, 201)
        self.assertIn("successfully added business", str(res.data))

    # def test_can_update_business(self):
    #     """Test API can create Business(POST request) """
    #     tester = app.test_client(self)
    #     res = tester.put('/api/auth/businesses/businessid', data= json.dumps(self.business))
    #     self.assertEqual(res.status_code, 201)
    #     self.assertIn("Kagz", str(res.data))

    def test_password_reset(self):
        """Test API can create Business(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/auth/reset-password', data= json.dumps(self.login))
        self.assertEqual(res.status_code, 201)
        self.assertIn("12345", str(res.data))

if __name__ == '__main__':
    unittest.main()