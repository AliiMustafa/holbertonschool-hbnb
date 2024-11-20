from backend.models.basemodel import BaseModel

class Review(BaseModel):
    def __init__(self,
                 text: str,
                 rating: int,
                 place: object,
                 user: object
    ):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
