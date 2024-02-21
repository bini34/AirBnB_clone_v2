#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy


class Amenity(BaseModel, Base):
    """blue print for amenity"""
    __tablename__ = 'amenities'
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
