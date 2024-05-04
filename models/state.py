#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """ Returns the list of City instances with
            state_id equals to the current State.id """
            cities = models.storage.all(City)
            lst = []
            for city in cities.values():
                if city.state_id == self.id:
                    lst.append(city)
            return lst
=======
"""The state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,delete,delete-orphan",
        backref=backref("state", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns list of City instances with state_id"""
            from models import storage
            from models import City
            return [v for k, v in storage.all(City).items()
                    if v.state_id == self.id]
>>>>>>> 173299cc64512fd3d380685dd99b53b3f044ffaa
