from backend.models.basemodel import BaseModel
from backend.models.users import User

class Place(BaseModel):
    def __init__(self,
                 title: str,
                 description: str,
                 price: float,
                 latitude: float,
                 longitude: float,
                 owner: User
    ):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []


    def add_review(self, review):
        """Add a review to the place"""
        self.reviews.append(review)

    def add_amenity(self, amenity_name):
        """Add an amenity to the place"""
        self.amenities.append(amenity_name)

    def to_dict(self):
        """Convert the User instance into a dictionary."""
        my_dict = super().to_dict()
        amenities = []
        for amenity_id in self.amenities:
            from backend.services import facades
            amen = facades.get_amenity(amenity_id)
            amen = amen.to_dict()
            amenities.append(amen)
        my_dict.update({
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": self.owner.to_dict(),
            "amenities": amenities
        })
        return my_dict

    def to_dict_wth_id(self):
        my_dict = super().to_dict()
        my_dict.update({
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner.id
        })
        return my_dict

    def to_dict_small(self):
        """Convert the User instance into a dictionary."""
        my_dict = super().to_dict()
        my_dict.update({
            "id": self.id,
            "title": self.title,
            "latitude": self.latitude,
            "longitude": self.longitude,
        })
        return my_dict
