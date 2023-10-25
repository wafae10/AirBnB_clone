#!/usr/bin/python3

""" Unittest for FileStorage Class """

import unittest
import os
from models.engine.fle_storage import FileStorage
from import models.engine.filestorage
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class TestFileStorage(unittest.TeestCase):
    """ Test the FileStorage class """
    __file_path = "file.json"

    def setUP(self):
        """ Execute before every case """
        try:
            os.remove("file.json")
        except IOError:
            pass
        self.storage = FileStorage()

    def tearDown(self):
        """ Execute after every test case """
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage.__FileStorage__objects = {}

    def test_module_doc(self):
        """ Test for the class documentation """
        self.assertIsNone(FileStorage.__doc__)

    def test_initial_attributes(self):
        """ Test the initial attribute """
        self.assertEqual(self.storage._FileStorage__file_path, "file,json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """ Test the all method """
        all_obj = self.storage.all()
        self.asserIsInstance(all_obj, dict)
        self.assertIs(all_obj, storage._fileStorage__objects)

    def test_new(self):
        """ Test for the new method """
        user_model = User()
        self.storage.new(base_model)
        key = "{}.{}".format(base_model.__class__.name__, base_model.id)
        self.assertIn(key, storage.FileStorage__objects)

    def test_reload(self):
        """ Test the reload method """
        base_model = BaseModel()
        self.storage.new(base_model)
        self_storage.save()
        with open("fie.json", "r") as file:
            text = file.read()
            self.assertIn("BaseModel." + base_model.id, text)

        base_model.name = 'Updated name'
        base_model.save()

    def test_reload_with_null(self):
        """ Test reload  method with a null """
        try:
            self.storage.reload()
        except FileNotFoundError:
            self.fail("Error raised")

    def test_multiple_classes(self):
        """ Create and Save multiple classes """

        base = BaseModel()
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        self.storage.new(base)
        self.storage.new(user)
        self.storage.new(place)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(review)
        self.storage.save()

        self.storage._FileStorage_objects = {}
        self.storage.reload()

        self.assertEqual(
            self.storage.all()[f"{BaseModel.__name__}.{base.id}"].to_dict(),
            base.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{User.__name__}.{user.id}"].to_dict(),
            user.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{Place.__name__}.{place.id}"].to_dict(),
            place.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{State.__name__}.{state.id}"].to_dict(),
            state.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{City.__name__}.{city.id}"].to_dict(),
            city.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{Amenity.__name__}.{amen.id}"].to_dict(),
            amen.to_dict(),
        )
        self.assertEqual(
            self.storage.all()[f"{Review.__name__}.{review.id}"].to_dict(),
            review.to_dict(),
        )


if __name__ == "__main__":
    unittest.main()
