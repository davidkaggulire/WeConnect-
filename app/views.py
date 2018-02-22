"""views.py"""

from app import app
from flask import request, jsonify, make_response, session
from app.models import User, Business, Signup

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    return "message"

@app.route('/api/auth/register', methods=['POST'])
def register():
    """" tests register user """
    test_user = request.get_json(force=True)
    id = test_user.get('id')
    firstname = test_user.get('firstname')
    lastname = test_user.get('lastname')
    username = test_user.get('username')
    password = test_user.get('password')
    email = test_user.get('email')
    phonenumber = test_user.get('phonenumber')
    gender = test_user.get('gender')

    if id and username:
        newUser = Signup(id=id, firstname=firstname, lastname=lastname, username=username, password=password, email=email, phonenumber=phonenumber, gender=gender )
        response = jsonify({
        'id': newUser.id,
        'firstname': newUser.firstname,
        'lastname': newUser.lastname,
        'username': newUser.username,
        'email': newUser.email,
        'password': newUser.password,
        'gender': newUser.gender,
        'phonenumber': newUser.phonenumber
    })

        user_message = {
            "message": "user successfully added"
        }
        response.status_code = 201
        return make_response(jsonify(user_message)), response.status_code

@app.route('/api/auth/login', methods=['POST'])
def login():  
    """tests user login"""

    login_user = request.get_json(force=True)      
    id = login_user.get('id')
    username = login_user.get('username')
    password = login_user.get('password')
    message = login_user.get('message')
    status = login_user.get('status')
    
    if id and username and password:
        new_user = User(id=id, username=username, password=password, message = '', status = '')        
        user = User(id = 1, username = 'david', password = 'abcd123', message = '', status = '')
        if new_user.username == user.username and new_user.password == user.password:
            res = jsonify({
                "username": new_user.username,
                "password": new_user.password,
                "message":'successfully logged in',
                'status': 'true'
            })
            res.status_code = 201
            return res
        else:
            return make_response(jsonify({'message': 'Invalid username or password'})), 403
    else:
        return make_response(jsonify({"message": "Please fill in username and password"})), 403
        
@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """tests user logout"""

    user = User(id=1,username='david', password='abcd123', message='', status='')
    if user:
        if user.password:
            response = jsonify({
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "message": "logged in",
                "status": "false"
            })
            return response
    

    
@app.route('/api/businesses', methods=['POST'])
def add_businesses():
    """tests register business """

    business = request.get_json(force = True)
    id = business.get('id')
    businessname = business.get('businessname')
    category = business.get('category')
    location = business.get('location')
    email = business.get('email')
    address = business.get('address')
    phonenumber = business.get('phonenumber')

    if id and email:
        new_business = Business(id=id, businessname=businessname, category=category, location=location, 
        email=email, address=address, phonenumber=phonenumber)

        response = jsonify({
            'id': new_business.id,
            'businessname': new_business.businessname,
            'location': new_business.location,
            'category': new_business.category,
            'email': new_business.email,
            'address': new_business.address,
            'phonenumber': new_business.phonenumber
        })
        return make_response(jsonify({'message': 'successfully added business'})), 201

@app.route('/api/businesses/<business_id>', methods=['GET', 'POST'])
def specific_business():
  pass
