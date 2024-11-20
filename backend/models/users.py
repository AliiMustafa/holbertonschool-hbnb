from backend.models.basemodel import BaseModel

class User(BaseModel):
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 email: str
    ):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False

