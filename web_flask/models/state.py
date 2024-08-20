class State(BaseModel, Base):
    # Existing code...

    @property
    def cities(self):
        """Return the list of City objects linked to the current State."""
        all_cities = storage.all(City)
        return [city for city in all_cities.values() if city.state_id == self.id]
