from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
import uuid
import datetime

Base = declarative_base()

class BaseModel:
    """Base class for all models."""

    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def save(self):
        """Saves the object to the database."""
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes the object from the database."""
        storage.delete(self)

    def to_dict(self):
        """Returns a dictionary representation of the object."""
        dict_rep = {}
        for column in self.__table__.columns:
            dict_rep[column.name] = getattr(self, column.name)
        dict_rep['__class__'] = self.__class__.__name__
        return dict_rep
