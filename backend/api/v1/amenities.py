from flask_restx import Namespace, Resource, fields
from backend.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload
        existing_amenity = facade.get_all_amenities()
        for amenity in existing_amenity:
            if amenity_data['name'] == amenity.name:
                return {'Error': 'Amenity already exists'}, 400
        new_amenity = facade.create_amenity(amenity_data)
        return {'id': new_amenity.id, 'name': new_amenity.name}, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        existing_amenity = facade.get_all_amenities()
        all_amenities = []
        [all_amenities.append({'id': amenity.id, 'name': amenity.name}) for amenity in existing_amenity]
        return all_amenities, 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'Error': 'Amenity not found'}, 404
        return {'id': amenity.id, 'name': amenity.name}, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Get amenity details by ID"""
        amenity_data = api.payload
        amenity = facade.get_amenity(amenity_id)
        if amenity_data['name'] == amenity['name']:
            return {'Message': 'Amenity also exists'}, 400
        amenity['name'] = amenity_data['name']
        return {'Message': 'Amenity updates successfully'}, 200
