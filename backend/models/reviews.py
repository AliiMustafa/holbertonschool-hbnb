from backend.models.basemodel import BaseModel
from backend.models.places import Place
from backend.models.users import User

class Review(BaseModel):
    def __init__(self,
                 text: str,
                 rating: int,
                 place: Place,
                 user: User
    ):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def to_dict_with_id(self):
        my_dict = super().to_dict()
        my_dict.update({
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user.id,
            "place_id": self.place.id
        })
        return my_dict

    def to_dict(self):
        my_dict = super().to_dict()
        my_dict.update({
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user.id,
            "place_id": self.place.id
        })
        return my_dict

    def to_dict_with_small(self):
        my_dict = super().to_dict()
        my_dict.update({
            "id": self.id,
            "text": self.text,
            "rating": self.rating
        })
        return my_dict