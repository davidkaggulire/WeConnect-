#models.py


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'david', 'dave123'),
    User(2, 'peter', 'pete123'),
]


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

class Signup(object):
    def __init__(self, id, firstname, lastname, username, password, email, gender):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password 
        self.email = email
        self.gender = gender

    def __str__(self):
        return "Signup(id = '%s')" % self.id

class Reviews(object):
    def __init__(self, id, review):
        self.id = id
        self.review = review

    def __str_(self):
        return "Review (id = '%s') " % self.id