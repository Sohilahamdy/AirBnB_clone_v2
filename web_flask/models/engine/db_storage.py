class DBStorage:
    # Existing code...

    def close(self):
        """Call remove() method on the private session attribute (self.__session)."""
        self.__session.remove()
