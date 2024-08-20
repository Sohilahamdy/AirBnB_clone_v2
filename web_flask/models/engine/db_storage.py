from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City

class DBStorage:
    """Handles SQLAlchemy database interactions."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine('mysql+mysqldb://user:password@localhost/db_name')
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage."""
        if cls is None:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
        else:
            objs = self.__session.query(cls).all()
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """Adds new object to storage."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commits all changes to the database."""
        self.__session.commit()

    def reload(self):
        """Reloads all objects from the database."""
        self.__session.remove()

    def delete(self, obj=None):
        """Deletes an object from storage."""
        if obj:
            self.__session.delete(obj)
            self.save()

    def close(self):
        """Removes the session."""
        self.__session.remove()
