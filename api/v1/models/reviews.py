""" reviews.py """

from flask import jsonify
reviews_list = []
class Reviews():
    def post_review(self, business_id, new_review):
        """ post review about business """
        reviews = {}
        for review in reviews_list:
            if review['business_id'] == business_id:
                return "Business already reviewed"
        else:
            reviews['business_id'] = business_id
            reviews['new_review'] = new_review
            reviews_list.append(reviews)
            return "Successfully added review"

    def get_reviews(self, business_id):
        """ get reviews about business """
        for review in reviews_list:
            if review['business_id'] == business_id:
                return review
        
        return reviews_list