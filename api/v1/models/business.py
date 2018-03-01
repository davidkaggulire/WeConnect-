""" business.py """
import uuid

class Business():
    """ class to handle business operations """
    def __init__(self):
        """ empty list to hold business objects """
        self.business_list = []

    def register(self, businessname, category, address, email, description ):
        """ registers business """
        #dictionary to hold business details
        business_details = {}

        for business in self.business_list:
            if business['businessname'] == businessname:
                return "Business exists"
        else:
            business_details['id'] =uuid.uuid1()
            business_details['businessname'] = businessname
            business_details['category'] = category
            business_details['address'] = address
            business_details['email'] = email
            business_details['description'] = description
            self.business_list.append(business_details)
            return "Business successfully created"
    
    # @staticmethod
    def view_all_businesses(self):
        """ method to reurn all businesses """
        return self.business_list

    def get_business_by_id(self, id ):
        """ getting business by id """
        self.id = id
        for business in self.business_list:
            if business['id'] == id:
                return business
                
    def update_business_by_id(self, businessname, category, address, email, description):
        """updating user by id"""
        for business in self.business_list:
            if business['id'] == id:
                business['businessname'] = businessname
                business['category'] = category
                business['address'] = address
                business['email'] = email
                business['description'] = description
                # self.business_list(business)
                return "Business updated successfully"

            else:
                message = "Business does not exist"
                return message
        else:
            return "You have no user credentials"

    def delete_business(self, id):
        """ Deletes business by id """
        self.id = id
        for business in self.business_list:
            if business['id'] == id:
                self.business_list.remove(id)
                return "Business successfully deleted"
        else:
            return "User credentials needed"