#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class User"""
from os import getenv

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all, delete", backref="user")
        review = relationship("Review", cascade="all, delete", backref="user")

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
=======
"""The user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship(
        "Place",
        cascade="all,delete",
        backref=backref("user", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)
    # TODO: wtf single_parent
    reviews = relationship(
        "Review",
        cascade="all,delete",
        backref=backref("user", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)
>>>>>>> 173299cc64512fd3d380685dd99b53b3f044ffaa
