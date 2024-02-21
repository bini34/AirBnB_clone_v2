#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import sqlalchemy


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    first_name = sqlalchemy.Column(sqlalchemy.String(128))
    last_name = sqlalchemy.Column(sqlalchemy.String(128))

    places = sqlalchemy.orm.relationship(
        "Place", backref="user", cascade="all, delete-orphan")
    reviews = sqlalchemy.orm.relationship(
        "Review", backref="user", cascade="all, delete-orphan")
