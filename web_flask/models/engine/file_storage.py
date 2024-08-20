import json

class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'  # Adjust this path as needed
        self.__objects = {}
        self.reload()  # Ensure this method exists

    def reload(self):
        """Reloads the stored objects from the JSON file."""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass

    def all(self, cls=None):
        """Returns a dictionary of all objects."""
        if cls is None:
            return self.__objects
        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """Adds a new object to the storage."""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Saves the objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def close(self):
        """Calls the reload method to load objects from the file."""
        self.reload()
