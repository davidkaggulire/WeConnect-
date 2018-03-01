""" views.py """
from werkzeug.security import generate_password_hash, check_password_hash
from api.v1 import app
from flask import request, jsonify, make_response, session
from api.v1.models.user import User
from api.v1.models.business import Business
from api.v1.models.reviews import Reviews

user_obj = User()
business_obj = Business()
review_obj = Reviews()
@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    return "message"

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    """ register user """
    test_user = request.get_json(force=True)
    firstname = test_user.get('firstname')
    lastname = test_user.get('lastname')
    username = test_user.get('username')
    password = test_user.get('password')
    hashed_password = generate_password_hash(password, method='sha256')
    email = test_user.get('email')
    gender = test_user.get('gender')
    
    if (firstname == "" or lastname == "" or username == "" or password == "" 
        or email == "" or gender == ""):
        message = "All fields required"
        return jsonify({"message":message})

    for user in user_obj.user_list:
        if user['username'] == username or user['email'] == email:
            return jsonify({"message": "User exists"})
    else:
        new_user = user_obj.register( firstname, lastname, username, hashed_password, email, gender)

        if new_user == "User successfully added":
            return jsonify(response=new_user), 201

@app.route('/api/v1/auth/login', methods=['POST'])
def login():  
    """tests user login"""

    login_user = request.get_json(force=True)      
    username = login_user.get('username')
    password = login_user.get('password')
    hashed_password = generate_password_hash(password)

    if username == '' or password == '':
        message = "All fields required"
        return jsonify({"message": message})

    # login_res = user_obj.login(username, password)
    # if login_res:
    for user in user_obj.user_list:
        if check_password_hash(user['password'], password):
            return jsonify({"message": "User successfully logged in", "success": True})
            
    else:
        return make_response(jsonify({'message': 'Invalid username or password'})), 403   
        
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """ tests user logout """
    login_user = request.get_json(force=True)  
    id = login_user.get('id')
    logout_user = user_obj.logout(id)
    if logout_user == "User logged out":
        return jsonify(response = logout_user), 200
    else:
        return make_response(jsonify({'message': 'Invalid username or password'})), 403   

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def password_reset():
    """ resets password of user """
    login_user = request.get_json(force=True)      
    username = login_user['username']
    password = login_user['password']
    hashed_password = generate_password_hash(password)

    for user in user_obj.user_list:
        if user['username'] == username:
            new_pass = user_obj.password_reset(username, hashed_password)
            if new_pass == "Password reset successfully":
                return jsonify(response=new_pass), 201
        else:
            return jsonify({"message": "Unknown user"}), 200
    
@app.route('/api/v1/businesses', methods=['POST', 'GET'])
def add_businesses():
    """ tests register business """
    if request.method == 'POST':
        business_user = request.get_json(force = True)
        businessname = business_user['businessname']
        category = business_user['category']
        email = business_user['email']
        address = business_user['address']
        description = business_user['description']

        if (businessname == "" or category == "" or email == "" or address == ""
            or description == "" ):
            message = "All fields required"
            return jsonify({"message": message})

        for business in business_obj.business_list:
            if business['businessname'] == businessname:
                message = "Business exists already"
                return jsonify(response=message)
        else:
            new_business = business_obj.register(businessname, category, address, email, description)

            if new_business == "Business successfully created":
                return jsonify(response=new_business), 201
            else:
                return jsonify(response=new_business),400

    elif request.method == 'GET':
        """ get all businesses """
        business = business_obj.view_all_businesses()
        return jsonify(business)
        

@app.route('/api/v1/businesses/<business_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def specific_business(business_id):
    if request.method == 'GET':
        for business in business_obj.business_list:
            if business['id'] == business_id:
                new_business = business_obj.get_business_by_id(business_id)
                return jsonify(new_business)

    elif request.method == 'PUT':
        business_user = request.get_json(force = True)
        businessname = business_user['businessname']
        category = business_user['category']
        email = business_user['email']
        address = business_user['address']
        description = business_user['description']

        for business in business_obj.business_list:
            if business['id'] == business_id:
                update_business = business_obj.update_business_by_id(businessname, 
                category, address, email, description)
                if update_business == "Business updated successfully":
                    return jsonify(update_business), 200
                else:
                    return "none"    

    elif request.method == 'DELETE':
        for business in business_obj.business_list:
            if business['id'] == business_id:
                del_business = business_obj.delete_business(business_id)
                if del_business == "Business successfully deleted":            
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
        review_input = review_user['review']

        for review_data in review_obj.reviews_list:
            if review_data['business_id'] == business_id:
                message = "user already reviewed business"
                return jsonify(message)

        else:
            add_review = review_obj.post_review(business_id, review_input)
            if add_review == "Successfully added review":
                return jsonify(add_review), 201
        
    elif request.method == 'GET':
        """ Getting reviews for businessid"""
        review_user = review_obj.get_reviews(business_id)  
        if review_user == "":          
            return jsonify(review_user)
        else:
            message = "User already added review"
            return jsonify(message)