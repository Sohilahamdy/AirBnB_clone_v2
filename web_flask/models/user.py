# models/user.py
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

class User(Base, BaseModel):
    """A class representing a user in the system."""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance."""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return a string representation of the User instance."""
        return "[User] ({}) {}".format(self.id, self.__dict__)
