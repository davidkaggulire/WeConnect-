#models.py


class User(object):
    def __init__(self, id, username, password, message, status):
        self.id = id
        self.username = username
        self.password = password
        self.message = message
        self.status = status

    def password_reset(self, password, ):
        self.password = password
        return "password has been reset"

    def __str__(self):
        return "User(id='%s')" % self.id

class Business(object):
    def __init__(self, id, businessname, location, category, address, email, phonenumber):
        self.id = id
        self.businessname = businessname
        self.location = location
        self.category = category
        self.address = address
        self.email = email
        self.phonenumber = phonenumber

    def __str__(self):
        return "Business(id='%s')"%self.id

    def update_registered_business(self, id, businessname, location, category, address, email, phonenumber):
        pass        

class Signup(object):
    def __init__(self, id, firstname, lastname, username, password, email, phonenumber, gender):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password 
        self.email = email,
        self.phonenumber = phonenumber
        self.gender = gender

    def __str__(self):
        return "Signup(id = '%s')" % self.id

class Reviews(object):
    def __init__(self, id, review):
        self.id = id
        self.review = review

    def __str_(self):
        return "Review (id = '%s') " % self.id