from flask_restx import Namespace, Resource, fields
from backend.services import facades

api = Namespace('places', description='Place operations')

# # Define the models for related entities
# amenity_model = api.model('PlaceAmenity', {
#     'id': fields.String(description='Amenity Id'),
#     'name': fields.String(description='Name of amenity')
# })
#
# user_model = api.model('PlaceUser', {
#     'id': fields.String(description='User Id'),
#     'first_name': fields.String(description='First name of the owner'),
#     'last_name': fields.String(description='Last name of the owner'),
#     'email': fields.String(description='Email of the owner')
# })

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(required=True, description='Description of the place'),
    'price': fields.String(required=True, description='Price of the place'),
    'latitude': fields.String(required=True, description='Latitude of the place'),
    'longitude': fields.String(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of the amenities ID's")
})

@api.route('/')
class PLaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        if float(place_data['price']) < 0:
            raise ValueError("Price must be 0 or above")
        if float(place_data['latitude']) < -90 and float(place_data['latitude']) > 90:
            raise ValueError("Latitude must be between -90 and 90")
        if float(place_data['longitude']) < -180 and float(place_data['longitude']) > 180:
            raise ValueError("Longitude must be between -180 and 180")
        owner_id = place_data['owner_id']
        place_data.pop('owner_id')
        amenities = [amenity for amenity in place_data['amenities']]
        place_data.pop('amenities')
        place_data['owner'] = facades.get_user(owner_id)
        new_place = facades.create_place(place_data)
        for amen in amenities:
            new_place.add_amenity(amen)
        return new_place.to_dict_wth_id(), 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        existing_places = facades.get_all_places()
        all_places = []
        [all_places.append(place.to_dict_small()) for place in existing_places]
        return all_places, 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        place = facades.get_place(place_id)
        if not place:
            return {'Error': 'Place not found'}, 404
        return place.to_dict(), 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Get place details by ID"""
        place = facades.get_place(place_id)
        if not place:
            return {'Error': 'Place not found'}, 404
        place_data = api.payload
        if place.title == place_data['title']:
            return {'Error': 'This place already exits'}, 400
        facades.update_place(place_id, place_data)
        return {'Message': 'Place updated successfully'}, 200
