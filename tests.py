""" tests.py """
from api.v1 import app
# import unittest
import unittest
import json

class BaseTestCase(unittest.TestCase):
    def createapp_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        """Define test variables and initialize app."""
        # tester = app.test_client(self)
        self.user = {
            "firstname": "christine",
            "lastname": "nakyobe",
            "username": "christine",
            "email": "xtine@gmail.com",
            "password": "abcd",
            "gender": "female"
        }
        # {
            
        #     "username": "christine",
            
        #     "password": "abcd"
        # }


        # {
        #     "firstname": "david",
        #     "lastname": "kaggulire",
        #     "username": "dkaggs",
        #     "email": "dkaggulire@gmail.com",
        #     "password": "hello",
        #     "gender": "male"
        # }

# {
#             "firstname": "abbey",
#             "lastname": "brooks",
#             "username": "abby",
#             "email": "abbey@gmail.com",
#             "password": "abey",
#             "gender": "male"
#         }

        self.business = {
            "businessname":"Kagz",
            "category":"electronics",
            "email":"kagz@gmail.com",
            "address":"kampala",
            "description":"We sell electronics"
        }
        # {
        #     "businessname":"Frisk",
        #     "category":"electronics",
        #     "email":"frisk@gmail.com",
        #     "address":"kampala",
        #     "description":"We sell electronics"
        # }
        # {
        #     "businessname":"Frisk",
        #     "category":"electronics",
        #     "email":"frisk@gmail.com",
        #     "address":"mukono",
        #     "description":"We sell electronics"
        # }
        self.reviews = {
            'business_id':'1',
            'reviews': 'Great services'
        }

class UserTestCase(BaseTestCase):
    """This class represents the users test case """
        
    def test_API_create_User(self):
        """Test API can create a User (POST request)"""
        tester = app.test_client(self)
        res = tester.post('/api/v1/auth/register', data= json.dumps(self.user), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("User successfully added", str(res.data))

    def test_API_user_login(self):
        """Test API can login User (POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/v1/auth/login', data= json.dumps(self.user), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn("User successfully logged in", str(res.data))

    # def test_API_user_logout(self):
    #     """Test API can logout(POST request) """
    #     tester = app.test_client(self)
    #     res = tester.post('/api/v1/auth/logout', data= json.dumps(self.user), content_type='application/json' )
    #     self.assertEqual(res.status_code, 200)
    #     self.assertIn("User logged out", str(res.data))

    def test_can_create_business(self):
        """Test API can create Business(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/v1/businesses', data= json.dumps(self.business), content_type='application/json' )
        self.assertEqual(res.status_code, 201)
        self.assertIn("Business successfully created", str(res.data))

    def test_get_businesses(self):
        """Test API get Business(GET request) """
        tester = app.test_client(self)
        res = tester.get('/api/v1/businesses')
        self.assertEqual(res.status_code, 200)
        

    def test_get_businesses_by_id(self):
        """Test API can get Business by ID (GET request) """
        tester = app.test_client(self)
        res = tester.get('/api/v1/businesses/1')
        self.assertEqual(res.status_code, 200)
        
    
    def test_can_update_business(self):
        """ Test API can update business by id """
        tester = app.test_client(self)
        res = tester.put('/api/v1/businesses/1', data= json.dumps(self.business), content_type='application/json')
        self.assertEqual(res.status_code, 200)     

    def test_delete_business_by_id(self):
        """ Test API can delete business by id """
        tester = app.test_client(self)
        # add_res = tester.post('/api/v1/business/1', data = json.dumps(self.business), content_type='application/json')
        # self.assertEqual(add_res.status_code, 201)
        res = tester.delete('/api/v1/businesses/1', content_type = 'application/json')
        self.assertEqual(res.status_code, 200)

    def test_password_reset(self):
        """Test API can create Business(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/v1/auth/reset-password', data= json.dumps(self.user), content_type = 'application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("Password reset successfully", str(res.data))
    
    # def test_post_review_by_business_id(self):
    #     """ Test API add review to business by business id """
    #     tester = app.test_client(self)
    #     res = tester.post('/api/v1/businesses/1/reviews', data = json.dumps(self.reviews), content_type = 'application/json')
    #     self.assertEqual(res.status_code, 201)
    #     self.assertIn("Successfully added review", str(res.data))

    # def test_get_reviews_for_business(self):
    #     """ Test API get reviews about business """
    #     tester = app.test_client(self)
    #     res = tester.get('api/v1/businesses/1/reviews', content_type = 'application/json')
    #     self.assertEqual(res.status_code, 200)
    #     self.assertIn("Great services", str(res.data))

if __name__ == '__main__':
    unittest.main()