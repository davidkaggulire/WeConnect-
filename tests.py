""" tests.py """
from api.v1 import app
# import unit test
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
            "id": "1",
            "firstname": "christine",
            "lastname": "nakyobe",
            "username": "christine",
            "email": "xtine@gmail.com",
            "password": "abcd",
            "gender": "female"
        }

        self.business = [{
            "id":1,
            "businessname":"Kagz",
            "location": "Kampala",
            "category":"electronics",
            "email":"kagz@gmail.com",
            "address":"P.O.Box 2334",
            "description":"We sell electronics"
        },
        {
            "id":2,
            "businessname":"Bolts",
            "location": "Kampala",
            "category":"hardware",
            "email":"bolts@gmail.com",
            "address":"P.O.Box 2444",
            "description":"We sell bolts, screws and nuts"
        }]
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

    def test_API_user_logout(self):
        """Test API can logout(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/v1/auth/logout', data= json.dumps(self.user), content_type='application/json' )
        self.assertEqual(res.status_code, 200)
        self.assertIn("You are now logged out", str(res.data))

    def test_can_create_business(self):
        """Test API can create Business(POST request) """
        tester = app.test_client(self)
        res = tester.post('/api/v1/businesses', data= json.dumps(self.business), content_type='application/json' )
        self.assertEqual(res.status_code, 201)
        self.assertIn("Business successfully created", str(res.data))

    # def test_get_businesses(self):
    #     """Test API get Business(GET request) """
    #     tester = app.test_client(self)
    #     res = tester.get('/api/v1/businesses')
    #     self.assertEqual(res.status_code, 200)
    #     self.assertIn("Kagz", str(res.data))

    # def test_get_businesses_by_id(self):
    #     """Test API can get Business by ID (GET request) """
    #     tester = app.test_client(self)
    #     res = tester.get('/api/v1/businesses/1')
    #     self.assertEqual(res.status_code, 200)
    #     # self.assertIn("Kagz", str(res.data))
    
    # def test_can_update_business(self):
    #     """ Test API can update business by id """
    #     tester = app.test_client(self)
    #     res = tester.put('/api/v1/businesses/1', data= json.dumps(self.business), content_type='application/json')
    #     self.assertEqual(res.status_code, 200)     

    # def test_delete_business_by_id(self):
    #     """ Test API can delete business by id """
    #     tester = app.test_client(self)
    #     # add_res = tester.post('/api/v1/business/1', data = json.dumps(self.business), content_type='application/json')
    #     # self.assertEqual(add_res.status_code, 201)
    #     res = tester.delete('/api/v1/businesses/1', content_type = 'application/json')
    #     self.assertEqual(res.status_code, 200)

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

    # def test_can_update_business(self):
    #     """ tests a business can be updated """
    #     tester = app.test_client(self)
    #     res = tester.post('/api/businesses', data = json.dumps(self.business), content_type = 'application/json')
    #     self.assertEqual(res.status_code, 201)
    #     new_data = {
    #         'id':'1',
    #         'businessname':'Davun',
    #         'location': 'Kampala',
    #         'category':'software',
    #         'email':'kagz@gmail.com',
    #         'address':'P.O.Box 2334',
    #         'phonenumber':'0704895678'
    #     }
    #     update_res = tester.put('/api/businesses/1', data = json.dumps(new_data), content_type = 'application/json')
    #     self.assertIn('Business updated successfully!', str(update_res.data))
    #     self.assertEqual(update_res.status_code, 200)


	# def test_deleting_registered_business(self):
	# 	""" tests a business can be deleted"""

	# 	business_data = {'id': 1, 'business_name': 'demo'}
	# 	rev = self.app.post('/api/v1/businesses', data = json.dumps(business_data), content_type = 'application/json')
	# 	self.assertEqual(rev.status_code, 201)
	# 	del_result = self.app.delete('/api/v1/businesses/1', content_type= 'application/json')
	# 	self.assertEqual(del_result.status_code, 200)


if __name__ == '__main__':
    unittest.main()