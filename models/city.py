#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete", backref="cities")

    else:
        state_id = ""
        name = ""
=======
"""The city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                      ForeignKey("states.id", ondelete="CASCADE"),
                      nullable=False)
    places = relationship(
        "Place",
        cascade="all",
        backref=backref("cities", cascade="all"),
        passive_deletes=True)
>>>>>>> 173299cc64512fd3d380685dd99b53b3f044ffaa
