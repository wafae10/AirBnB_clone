#!/usr/bin/python3

import json
import os

class FileStorage:
    """ This is the FileStorage class """
    
    #Private class attribute to store string-path to the JSON file
    __file_path = "file.json"

    # Private class attribute to store all objects by <class name>.id
    __objects = {}

    """def classes(self):
        from models.base_model import BaseModel
        temp = {'BaseModel': BaseModel, }
        return temp """


    #Public Instance

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new object to __objects dictionary """
        new_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[new_obj] = obj

    def save(self):
        """ This serializes __objects to JSON file """
        with open(FileStorage.__file_path, 'w') as f:
            obj_dict = {}
            for key, value in obj_dict.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """ This deserializes the JSON file to __objects """
        from models.base_model import BaseModel

        classes = {'BaseModel': BaseModel}
        """load_file = FileStorage.__file_path
        if os.path.exists(load_file):"""
        try:
            content = {}
            with open(FileStorage.__file_path, 'r') as f:
                content = json.load(f)
                for key, value in content.items():
                    self.all()[key] = classes()[value["__class"]](**value)
        except FileNotFoundError:
            pass
