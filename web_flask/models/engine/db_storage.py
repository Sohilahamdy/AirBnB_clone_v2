from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.state import State
from models.city import City

class DBStorage:
    """Handles storage in a database using SQLAlchemy."""
    
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the database engine and session."""
        self.__engine = create_engine('mysql+mysqldb://user:password@localhost/dbname')
        BaseModel.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Returns a dictionary of all objects or objects of a specific class."""
        if cls is None:
            objs = self.__session.query(State).all() + self.__session.query(City).all()
        else:
            objs = self.__session.query(cls).all()
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """Adds a new object to the session."""
        self.__session.add(obj)

    def save(self):
        """Commits the current session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the session."""
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """Reloads the session."""
        self.__session.remove()
