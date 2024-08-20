# models/base_model.py
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """A base class for all models with common attributes and methods."""

    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        pass

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the current instance to the database."""
        from models import storage
        storage.new(self)
        storage.save()

    def delete(self):
        """Delete the current instance from the database."""
        from models import storage
        storage.delete(self)
        
    def to_dict(self):
        """Convert the instance to a dictionary format."""
        d = self.__dict__.copy()
        d.update({"__class__": self.__class__.__name__})
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
