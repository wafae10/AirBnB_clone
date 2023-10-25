#!/usr/bin/python3
"""
This module define a class to manage file storage
The modue serializes objects to a JSON file and
deserialize JSON files to instances

Attributes:
    __file_path (str): A path that save objects
    __objects (dict): A dictionary of the objects instance.
"""

import json
import os


class FileStorage:
    """
    This is the FileStorage class that
    serialize and deserializes a file to an instance"""

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """ This function return the classes dictionary """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        temp = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }
        return temp

    def all(self):
        """ Returns all the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new object to __objects dictionary """
        new_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[new_obj] = obj

    def save(self):
        """ This serializes __objects to JSON file """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ This deserializes the JSON file to __objects """
        load_file = FileStorage.__file_path
        if os.path.exists(load_file):
            with open(FileStorage.__file_path, 'r') as f:
                content = json.load(f)
                for key, value in content.items():
                    obj = self.classes()[value["__class__"]](**value)
                    FileStorage.__objects[key] = obj
