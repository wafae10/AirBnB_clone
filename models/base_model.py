#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ This is a BaseModel Instance """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ Represent string function Instance """
        return "[{}] ({}) {}". format(self.__class__.__name__,
                                        self.id, self.__dict__)

    def save(self):
        """ To update the public instance attribute with current date time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ To return a dictionary containing all keys/values of __dict__
            of the instance """
        data = self.__dict__.copy()
        data['class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

