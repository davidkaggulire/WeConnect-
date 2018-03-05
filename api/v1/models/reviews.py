""" reviews.py """

from flask import jsonify

class Reviews():
    def __init__(self):
        self.reviews_list = []
    def post_review(self, business_id, new_review):
        """ post review about business """
        reviews = {}
        for review in self.reviews_list:
            if review['business_id'] == business_id:
                return "Business already reviewed"
        else:
            reviews['business_id'] = business_id
            reviews['new_review'] = new_review
            self.reviews_list.append(reviews)
            return "Successfully added review"
    def get_reviews(self, business_id):
        """ get reviews about business """
        for review in self.reviews_list:
            if review['business_id'] == business_id:
                return review
        
        return self.reviews_list