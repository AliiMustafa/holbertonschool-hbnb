from flask_restx import Namespace, Resource, fields
from backend.services import facades

api = Namespace('users', description='User operations')

#Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required = True, description='First name of the user'),
    'last_name': fields.String(required = True, description='Last name of the user'),
    'email': fields.String(required = True, description='Email of the user'),
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        #Simulate email uniqueness check( to be replaced by real validation with persistence)
        existing_user = facades.get_user_by_email(user_data['email'])
        if existing_user:
            return {'Error': 'Email already registered'}, 400

        new_user = facades.create_user(user_data)
        return new_user.to_dict(), 201

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facades.get_user(user_id)
        if not user:
            return {'Error': 'User not found'}, 404
        return user.to_dict(), 200

