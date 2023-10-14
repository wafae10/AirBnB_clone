#!/usr/bin/python3

import json
import os

class FileStorage:
    """ This is the FileStorage class """
    
    #Private class attribute to store string-path to the JSON file
    __file_path = "file.json"

    # Private class attribute to store all objects by <class name>.id
    __objects = {}

    def classes(self):
        from models.base_model import BaseModel
        temp = {'BaseModel': BaseModel, }
        return temp


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
