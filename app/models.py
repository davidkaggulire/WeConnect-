#models.py
from flask import jsonify

class User(object):
    def __init__(self):
        self.user_list = []

    def register(self, id, firstname, lastname, username, password, email, gender):
        """ registers user if user doesnot exist """
        user_details = {}

        for user in self.user_list:
            if user['username'] == username or user['email'] == email:        
                return "Username or email exists"
        else:
            user_details['id'] = id
            user_details['firstname'] = firstname
            user_details['lastname'] = lastname
            user_details['username'] = username
            user_details['password'] = password
            user_details['email'] = email
            user_details['gender'] = gender
            
            self.user_list.append(user_details)        
            return "User successfully added"

    def login(self, username, password):
        """ login user given valid credentials """
        for user in self.user_list:
            if user['username'] == username:
                if user['password'] == password:
                    return "User successfully logged in"
                else:
                    return "Incorrect credentials"
        return "User doesnot exist"

    def password_reset(self, username, newpassword):
        for user in self.user_list:
            if user['username'] == username:
                user['password'] = newpassword
                return "Password reset successfully"
        else:
            return "Failed to reset"


# class Reviews(object):
#     def __init__(self, id, review):
#         self.id = id
#         self.review = review

#     def __str_(self):
#         return "Review (id = '%s') " % self.id