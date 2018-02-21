#views.py

from app import *
from flask import request, jsonify
from app.models import User, Business, Signup, Reviews, users

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    return "message"

@app.route('/api/auth/register', methods=['GET', 'POST'])
def register():
    pass
    
@app.route('/api/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        user = users[].username
        return str(user)
   
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



