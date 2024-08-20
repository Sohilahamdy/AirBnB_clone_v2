from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """City class to represent a city in the AirBnB system."""

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')

    def __init__(self, *args, **kwargs):
        """Initialize a new City instance."""
        super().__init__(*args, **kwargs)
