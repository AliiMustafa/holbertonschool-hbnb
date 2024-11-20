from backend.models.amenities import Amenity
from backend.persistence.repository import InMemoryRepository
from backend.models.users import User
from backend.models.amenities import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        # self.review_repo = InMemoryRepository()
        # self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Placeholder method for fetching a place by ID
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.place_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.place_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.place_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        return self.place_repo.update(amenity_id, amenity_data)