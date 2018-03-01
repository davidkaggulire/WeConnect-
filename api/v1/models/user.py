#models.py
import uuid
from flask import jsonify, session
from werkzeug.security import generate_password_hash

class User():
    def __init__(self):
        self.user_list = []

    def register(self, firstname, lastname, username, password, email, gender):
        """ registers user if user doesnot exist """
        user_details = {}

        for user in self.user_list:
            if user['username'] == username or user['email'] == email:        
                return "Username or email exists"
        else:
            user_details['id'] = uuid.uuid1()
            user_details['firstname'] = firstname
            user_details['lastname'] = lastname
            user_details['username'] = username
            user_details['password'] = password
            user_details['email'] = email
            user_details['gender'] = gender
            session['username'] = username
            self.user_list.append(user_details)        
            return "User successfully added"

    def login(self, username, password):
        """ login user given valid credentials """
        for user in self.user_list:
            hashed_password = generate_password_hash(password)
            if user['username'] == username:
                if user['password'] == hashed_password:
                    return "User successfully logged in"
                else:
                    return
        return

    def password_reset(self, username, newpassword):
        for user in self.user_list:
            if user['username'] == username:
                hashed_password = generate_password_hash(newpassword)
                # user['password'] = newpassword
                user['password'] = hashed_password
                return "Password reset successfully"
        else:
            return "Failed to reset"

    def logout(self, id):
        """ logout user """
        for user in self.user_list:
            if user['id'] == id:
                session.pop(user['username'], None)
                return "User logged out"