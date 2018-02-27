""" views.py """

from app import app
from flask import request, jsonify, make_response, session
from app.models import User
from app.business import Business
from app.reviews import Reviews

user_obj = User()
business_obj = Business()
review_obj = Reviews()
@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    return "message"

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    """" tests register user """
    test_user = request.get_json(force=True)
    id = test_user['id']
    firstname = test_user['firstname']
    lastname = test_user['lastname']
    username = test_user['username']
    password = test_user['password']
    email = test_user['email']
    gender = test_user['gender']

    for user in user_obj.user_list:
        if user['username'] == username and user['password'] == password:
            return jsonify({"message": "User exists"})
    else:
        new_user = user_obj.register(id, firstname, lastname, username, password, email, gender)

        if new_user == "User successfully added":
            return jsonify(response=new_user), 201
        else:
            return jsonify(response=new_user), 200

@app.route('/api/v1/auth/login', methods=['POST'])
def login():  
    """tests user login"""

    login_user = request.get_json(force=True)      
    username = login_user['username']
    password = login_user['password']
    new_user = {
            "id": '1',
            "username": "christine",
            "password": "abcd",
        }
    login_res = user_obj.login(username, password)
    if new_user['username']== username and new_user['password'] == password:
        if login_res == "User successfully logged in":
            return jsonify(response=login_res), 200
        else:
            return make_response(jsonify({'message': 'Invalid username or password'})), 403   
    else:
        return "none"
        
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """ tests user logout """

    login_user = request.get_json(force=True)      
    username = login_user['username']
    password = login_user['password']
    new_user = {
            "id": '1',
            "username": "christine",
            "password": "abcd",
        }
    # login_res = user_obj.login(username, password)
    if new_user['username']== username and new_user['password'] == password:
            return jsonify("You are now logged out"), 200
    else:
        return make_response(jsonify({'message': 'Invalid username or password'})), 403   

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def password_reset():
    login_user = request.get_json(force=True)      
    username = login_user['username']
    password = login_user['password']

    new_pass = user_obj.password_reset(username, password)
    if new_pass == "Password reset successfully":
        return jsonify(response=new_pass), 201
    else:
        return jsonify(response=new_pass),400
    return jsonify(new_pass)
    
@app.route('/api/v1/businesses', methods=['POST', 'GET'])
def add_businesses():
    """ tests register business """
    if request.method == 'POST':
        business_users = request.get_json(force = True)
        business_user = business_users[0]
        id = business_user['id']
        businessname = business_user['businessname']
        category = business_user['category']
        location = business_user['location']
        email = business_user['email']
        address = business_user['address']
        description = business_user['description']

        for business in business_obj.business_list:
            if business['businessname'] == businessname:
                return jsonify("Business exists already")
        else:
            new_business = business_obj.register(id, businessname, location, category, address, email, description)

            if new_business == "Business successfully created":
                return jsonify(response=new_business), 201
            else:
                return jsonify(response=new_business),400

    elif request.method == 'GET':
        """ get all businesses """
        
        businesses = [{
            "id":"1",
            "businessname":"Kagz",
            "location": "Kampala",
            "category":"electronics",
            "email":"kagz@gmail.com",
            "address":"P.O.Box 2334",
            "description":"We sell electronics"
        },
        {
            "id":"2",
            "businessname":"Bolts",
            "location": "Kampala",
            "category":"hardware",
            "email":"bolts@gmail.com",
            "address":"P.O.Box 2444",
            "description":"We sell bolts, screws and nuts"
        }]
        
        business = business_obj.view_all_businesses(businesses)
        return jsonify(business)
        

@app.route('/api/v1/businesses/<business_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def specific_business(business_id):
    if request.method == 'GET':
        # business = {
        #     "id":"1",
        #     "businessname":"Kagz",
        #     "location": "Kampala",
        #     "category":"electronics",
        #     "email":"kagz@gmail.com",
        #     "address":"P.O.Box 2334",
        #     "description":"We sell electronics"
        # }
        new_business = business_obj.get_business_by_id(business_id)
        return jsonify(new_business)

    elif request.method == 'PUT':
        business_users = request.get_json(force = True)
        business_user = business_users[0]
        business_id = business_user['id']
        owner_id = business_user['id']
        businessname = business_user['businessname']
        category = business_user['category']
        location = business_user['location']
        email = business_user['email']
        address = business_user['address']
        description = business_user['description']

        business_data = {
            "id":1,
            "owner_id": 1,
            "businessname":"Kagz",
            "location": "Kampala",
            "category":"electronics",
            "email":"kagz@gmail.com",
            "address":"P.O.Box 2334",
            "description":"We sell electronics"
        }

        if business_data['id'] == business_id and business_data['id'] == owner_id:
            update_business = business_obj.update_business_by_id(business_id, owner_id, businessname, category,
        location, address, email, description)
            return jsonify(update_business), 200
        else:
            return "none"    

    elif request.method == 'DELETE' :
        business_data = {
            "id":1,
            "owner_id": 1,
            "businessname":"Kagz",
            "location": "Kampala",
            "category":"electronics",
            "email":"kagz@gmail.com",
            "address":"P.O.Box 2334",
            "description":"We sell electronics"
        }
        if business_data['id'] == business_id:
            del_business = business_obj.delete_business(business_id)
            return jsonify(del_business)
        else:
            message = "Cannot delete business"
            return jsonify(message)

@app.route('/api/v1/businesses/<business_id>/reviews', methods=['GET', 'POST'])
def review_business(business_id):
    """ Posting review for businessid """
    if request.method == 'POST':
        review_user = request.get_json(force=True)
        business_id = review_user['business_id']
        review_input = review_user['new_review']

        for review_data in review_obj.reviews_list:
            if review_data['business_id'] == business_id:
                return "user already reviewed business"

        else:
            add_review = review_obj.post_review(business_id, review_input)
            if add_review == "Successfully added review":
                return jsonify(add_review), 201
            else:
                return jsonify(add_review), 200
        
    elif request.method == 'GET':
        """ Getting reviews for businessid"""
        user_review = {
            "business_id": 1,
            "review": "Great services"
        }
        if user_review['business_id'] == business_id:
            review_user = review_obj.get_reviews(business_id)
            return jsonify(review_user)
        else:
            message = "User already added review"
            return jsonify(message)