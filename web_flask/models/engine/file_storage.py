import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage."""
        if cls is None:
            return FileStorage.__objects
        return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves objects to JSON file."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Loads objects from JSON file."""
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            objs = json.load(f)
            for k, v in objs.items():
                cls_name = v['__class__']
                cls = globals().get(cls_name)
                if cls:
                    FileStorage.__objects[k] = cls(**v)

    def delete(self, obj=None):
        """Deletes an object from storage."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

    def close(self):
        """Reloads storage from file."""
        self.reload()
