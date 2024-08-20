#!/usr/bin/python3
"""
State class module.
"""
from models.base_model import BaseModel
from models import storage

class State(BaseModel):
    """
    State class that inherits from BaseModel.
    Represents a state with a name.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new State instance.
        """
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """
        Returns a list of City instances associated with this State.
        """
        from models.city import City
        all_cities = storage.all(City).values()
        state_cities = [city for city in all_cities if city.state_id == self.id]
        return state_cities
