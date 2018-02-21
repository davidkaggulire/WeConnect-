"""views.py"""

from app import app
from flask import request, jsonify
from app.models import User, Business, Signup, Reviews, users

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    return "message"

@app.route('/api/auth/register', methods=['POST'])
def register():
    if request.method == "POST":
        test_user = request.get_json()
        id = test_user['id']
        firstname = test_user['firstname']
        lastname = test_user['lastname']
        username = test_user['username']
        password = test_user['password']
        email = test_user['email']
        phonenumber = test_user['phonenumber']
        gender = test_user['gender']

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
            response.status_code = 201
            return response
        else:
            return 'fail'

@app.route('/api/auth/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = {
            'id': 1,
            'username': 'xtine',
            'password': 'abcd'
        }
        return jsonify(user)
    else:
        return 'fail'

@app.route('/api/auth/logout', methods=['GET', 'POST'])
def logout():
    pass

@app.route('/api/reset-password', methods=['POST'])
def reset():
    if request.method == 'POST':
        newPassword = {
            'password': 'apple'
        }
        return jsonify(newPassword)

@app.route('/api/businesses/<business_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def specific_business():

    if request.method == 'GET':
        business = request.get_json()
        id = business['id']
        businessname = business['business']
        businesscategory = business['category']
        businesslocation = business['location']
        email = business['email']
        address = business['address']
        phonenumber = business['phonenumber']


        newBusiness = {
            'id':'1',
            'businessname':'Kagz',
            'location': 'Kampala',
            'category':'electronics',
            'email':'kagz@gmail.com',
            'address':'P.O.Box 2334',
            'phonenumber':'0704895678'
        }
        return newBusiness

        else:
            return "fail"
    elif request.method == 'POST':
        pass
    
    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass



