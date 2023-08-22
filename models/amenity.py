#!/usr/bin/python
""" Holds the Amenity class definition """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """ Representation of the Amenity class """
    AMENITY_STORAGE = 'db'

    if models.storage_t == AMENITY_STORAGE:
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes an instance of Amenity """
        super().__init__(*args, **kwargs)

