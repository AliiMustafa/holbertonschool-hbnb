from flask_restx import Namespace, Resource, fields
from backend.services import facades

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        # Placeholder for the logic to register a new review
        review_data = api.payload
        if not review_data:
            return {'Error': 'Invalid input data'}, 400
        user_id = review_data['user_id']
        place_id = review_data['place_id']
        review_data.pop('user_id')
        review_data.pop('place_id')
        review_data['user'] = facades.get_user(user_id)
        review_data['place'] = facades.get_place(place_id)
        new_review = facades.create_review(review_data)
        review_id = new_review.id
        new_review.place.add_review(review_id)
        return new_review.to_dict(), 201


    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        # Placeholder for logic to return a list of all reviews
        existing_reviews = facades.get_all_reviews()
        all_reviews = []
        [all_reviews.append(review.to_dict_with_small()) for review in existing_reviews]
        return all_reviews, 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        review = facades.get_review(review_id)
        if not review:
            return {'Error': 'No review found'}, 404
        return review.to_dict_with_id, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        # Placeholder for the logic to update a review by ID
        review = facades.get_place(review_id)
        if not review:
            return {'Error': 'Review not found'}, 404
        review_data = api.payload
        if review.text == review_data['text']:
            return {'Error': 'This review already exits'}, 400
        facades.update_place(review_id, review_data)
        return {'Message': 'Review updated successfully'}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        # Placeholder for the logic to delete a review
        if not facades.get_review(review_id):
            return {'Error': 'Invalid id'}, 400

        deleted_review = facades.delete_review(review_id)
        return {'Message': 'Review deleted successfully'}, 200

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Placeholder for logic to return a list of reviews for a place
        place = facades.get_place(place_id)
        reviews = []
        for review in place.reviews:
            review_obj = facades.get_review(review)
            reviews.append(review_obj.to_dict_with_small())
        return reviews, 200