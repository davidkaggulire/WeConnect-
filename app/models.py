#models.py


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

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



