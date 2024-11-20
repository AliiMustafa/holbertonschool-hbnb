from backend.models.basemodel import BaseModel

class Place(BaseModel):
    def __init__(self,
                 title: str,
                 description: str,
                 price: float,
                 latitude: float,
                 longitude: float,
                 owner: object
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
