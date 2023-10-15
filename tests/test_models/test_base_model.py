#!/usr/bin/python3
""" This module test for the Basemodel applications """
import unittest
from  model.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ This is to test the Basemodel class """

    def test_init(self):
        """ Tests the __init__ method. """
        model = BaseModel()
        self.assertGreater( datetime.now(), model.created_at)
        self.assertEqual(model.updated_at, model.created_at)

    def test_str(self):
        """ Tests the __str__ method """
        model = BaseModel()
        class_name = model.__class__.name__
        check_str = f"[{cass_name}] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), check_str)

    def test_save(self):
        """ Test the save method """
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)

    def test_to_dict(self):
        """ Test the to_dict method """
        model = BaseModel()
        dict_test = model.to_dict()
        self.assertEqual(dict_test['__class__'], model__.class__.__name__)
        self.assertEqual(dict_test['created_at'], model.created_at.isoformat())
        self.assetEqual(dict_test['updated_at'], model.updated_at.isoformat())
