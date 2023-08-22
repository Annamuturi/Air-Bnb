#!/usr/bin/python3
"""
Contains the BaseModel class, the foundation for other classes.
"""

from datetime import datetime
from models import storage
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

# Common format for datetime serialization
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

# Determine the base class based on the storage type
Base = declarative_base() if models.storage_t == "db" else object

class BaseModel(Base):
    """
    The BaseModel class from which all other classes inherit.
    Provides common attributes and methods.
    """
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Positional arguments (not used).
            **kwargs: Keyword arguments that can contain instance attributes.
        """
        if kwargs:
            self.__set_attributes(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __set_attributes(self, **kwargs):
        """
        Set instance attributes based on keyword arguments.

        Args:
            **kwargs: Keyword arguments containing instance attributes.
        """
        for key, value in kwargs.items():
            if key != "__class__":
                setattr(self, key, value)

        if isinstance(kwargs.get("created_at"), str):
            self.created_at = datetime.strptime(kwargs["created_at"], DATETIME_FORMAT)
        else:
            self.created_at = datetime.utcnow()

        if isinstance(kwargs.get("updated_at"), str):
            self.updated_at = datetime.strptime(kwargs["updated_at"], DATETIME_FORMAT)
        else:
            self.updated_at = datetime.utcnow()

        if not kwargs.get("id"):
            self.id = str(uuid.uuid4())

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: The string representation.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute and saves the instance to storage.
        """
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Converts instance attributes to a dictionary for serialization.

        Returns:
            dict: Dictionary containing instance attributes.
        """
        instance_dict = self.__dict__.copy()

        if "created_at" in instance_dict:
            instance_dict["created_at"] = self.created_at.strftime(DATETIME_FORMAT)

        if "updated_at" in instance_dict:
            instance_dict["updated_at"] = self.updated_at.strftime(DATETIME_FORMAT)

        instance_dict["__class__"] = self.__class__.__name__
        instance_dict.pop("_sa_instance_state", None)

        return instance_dict

    def delete(self):
        """
        Deletes the current instance from the storage.
        """
        storage.delete(self)

