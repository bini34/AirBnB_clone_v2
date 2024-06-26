#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
import models
from sqlalchemy import Integer, Table, String, Column, Float, ForeignKey
import os
from sqlalchemy.orm import relationship

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id', String(60), ForeignKey('places.id'), nullable=False),
    Column(
        'amenity_id', String(60), ForeignKey('amenities.id'), nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    ENV = os.getenv("HBNB_TYPE_STORAGE")
    if ENV == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            backref='place_amenities')
        reviews = relationship(
            "Review", backref="place", cascade="all, delete-orphan")

    else:
        amenity_ids = []

        @property
        def reviews(self):
            """ge all review"""
            return [
                review
                for review in models.storage.all('Review').values()
                if review.place_id == self.id
            ]

        @property
        def amenities(self):
            return [
                amenity
                for amenity in model.storage.all('Amenity').values()
                if Amenity.place_id == self.idi
            ]

        @amienities.setter
        def amenities(self):
            """all amenities"""
            Place.amenity_ids = [
                amienity
                for amenity in models.storage.all('Amenity').values()
                if amienity.place_id == self.id
            ]
