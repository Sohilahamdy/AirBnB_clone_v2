import json
from models.base_model import BaseModel

class FileStorage:
    """Handles the storage of objects in a JSON file."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects or objects of a specific class."""
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """Adds a new object to the storage."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves the objects to the JSON file."""
        with open(self.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """Loads objects from the JSON file."""
        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, obj_dict in objects_dict.items():
                    cls_name = obj_dict['__class__']
                    cls = globals().git[cls_name]
                    if cls:
                        self.__objects[key] = cls(**obj_dict)
        except FileNotFoundError:
            pass
