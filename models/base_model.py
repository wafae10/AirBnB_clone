#!/usr/bin/python3

"""
This module is for the BaseModel class for all other models in the application

Attributes:
    id: A unique identifier for each instance.
    created_at: This shows the time the instance is being created.
    updated_at: This will show the instance modified datetime.

    Methods:
    to_dict(): dictionary representation of the model
    save(): Saves the model to the database
    __str__(): string representation of the module
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ This is a BaseModel Instance """

    def __init__(self, *args, **kwargs):
        """ This function initialize BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.strptime
                                (value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """ Represent string function Instance """
        return "[{}] ({}) {}". format(self.__class__.__name__,
                                      self.id, self.__dict__)

    def save(self):
        """ To update the public instance
            attribute with current date time """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ To return a dictionary containing all keys/values
            of __dict__ of the instance """

        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
