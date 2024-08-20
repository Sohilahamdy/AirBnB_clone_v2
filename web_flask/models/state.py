from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """State class to represent a state in the AirBnB system."""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        """Initialize a new State instance."""
        super().__init__(*args, **kwargs)
