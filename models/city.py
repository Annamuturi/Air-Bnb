#!/usr/bin/python
"""Holds the City class definition."""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Representation of a city."""
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="city")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an instance of the City class."""
        super().__init__(*args, **kwargs)

