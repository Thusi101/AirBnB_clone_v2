#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv, remove

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
from sqlalchemy.orm.session import Session

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    """This class manages storage in a database."""

    __engine = None
    __session = None

    classes = [Amenity, City, Place, Review, State, User]

    def __init__(self):
        """Instantiates the DBStorage class"""

        mySQL_u = getenv("HBNB_MYSQL_USER")
        mySQL_p = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")

        url = {'drivername': 'mysql+mysqldb', 'host': db_host,
               'username': mySQL_u, 'password': mySQL_p, 'database': db_name}

        self.__engine = create_engine(URL(**url), pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in database"""
        objs = []
        dct = {}
        if cls is None:
            for item in self.classes:
                objs.extend(self.__session.query(item).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()

        for obj in objs:
            dct[obj.__class__.__name__ + '.' + obj.id] = obj
        return dct

    def new(self, obj):
        """Adds the object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables of the database"""
        Base.metadata.create_all(self.__engine)

        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()

    def close(self):
        """Handles close of DBStorage"""
=======
"""Module for DBstorage class"""
from os import getenv
from sqlalchemy import create_engine, MetaData


class DBStorage():
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes storage"""
        from models.base_model import Base
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
        """returns all objects of cls"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_list = [
            State,
            City,
            User,
            Place,
            Review,
            Amenity
        ]
        rows = []
        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in class_list:
                rows += self.__session.query(cls)
        return {type(v).__name__ + "." + v.id: v for v in rows}

    def new(self, obj):
        """add object to db"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """commit changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create all tables in the db"""
        from models.base_model import Base
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review
        from models.place import Place
        from sqlalchemy.orm import sessionmaker, scoped_session

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Thread specific storage"""
>>>>>>> 173299cc64512fd3d380685dd99b53b3f044ffaa
        self.__session.close()
