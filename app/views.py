#views.py

from app import *
from flask import request, jsonify
from app.models import User

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    return "message"

@app.route('/api/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        newUser = User(username = str(request.data.get('username'), password = str(request.data.get('password'))))
        response = jsonify({'username': newUser.username})
        response.status_code = 200
        return response

@app.route('/api/auth/login', methods=['POST'])
def login():
    pass
    # user = request.get_json()
    # userlogin = {}
    # userlogin['username'] = user['name']
    # userlogin['password'] = user['password']
    # return jsonify(userlogin)

@app.route('/api/auth/logout', methods=['GET', 'POST'])
def logout():
    pass

@app.route('/api/resetpassword', methods=['GET', 'POST'])
def reset():
    pass

@app.route('/api/businesses', methods=['GET', 'POST'])
def business():
    pass

@app.route('/api/businesses/<businessid>', methods=['GET', 'POST'])
def viewbusiness():
    pass

@app.route('/businesses/<businessid>', methods=['DELETE'])
def delelebusiness():
    pass

@app.route('/businesses/<businessId>/reviews', methods=['POST'])
def postreviews():
    pass



