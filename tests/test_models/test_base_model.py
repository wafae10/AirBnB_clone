#!/usr/bin/python3
""" This module test for the Basemodel applications """
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """ This is to test the Basemodel class """

    def test_init(self):
        """ Tests the __init__ method. """
        model = BaseModel()
        self.assertGreater(datetime.now(), model.created_at)
        self.assertEqual(model.updated_at, model.created_at)

    def test_str(self):
        """ Tests the __str__ method """
        model = BaseModel()
        class_name = model.__class__.__name__
        check_str = f"[{class_name}] ({model.id}) {model.__dict__}"
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
        self.assertEqual(dict_test['__class__'], model.__class__.__name__)
        self.assertEqual(dict_test['created_at'], model.created_at.isoformat())
        self.assertEqual(dict_test['updated_at'], model.updated_at.isoformat())

    def test_class_doc(self):
        """ Test BaseModel instance documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_method_docs(self):
        """ Test BaseModel methods documentation"""
        methods = [
            BaseModel.__init__, BaseModel.__str__,
            BaseModel.save, BaseModel.to_dict
        ]
        for a in methods:
            self.assertIsNotNone(a.__doc__)

    def test_initial_attribute(self):
        """ Test object id"""
        test_model = BaseModel()
        test_model_new = BaseModel()

        # check if id exists, not NULL and a string
        self.assertTrue(hasattr(test_model, 'id'))
        self.assertIsNotNone(test_model.id)
        self.assertIsInstance(test_model.id, str)

        # Check if id is uuid
        self.assertTrue(uuid.UUID(test_model.id))

        # Check if two instances have the same id
        self.assertNotEqual(test_model.id, test_model_new.id)

        # Check that *args was not used
        test_with_arg = BaseModel("args")
        self.assertNotIn("args", test_with_arg.__dict__)

        # Check if __str__ represent correct output
        str_ = "[BaseModel] ({}) {}".format(test_model.id, test_model.__dict__)
        self.assertEqual(str(test_model), str_)

        # Check if created_at exist, not NULL, and it's from datetime
        self.assertTrue(hasattr(test_model, 'created_at'))
        self.assertIsNotNone(test_model.created_at)
        self.assertIsInstance(test_model.created_at, datetime)

        # Check if updated_at exist, not NULL, and it's from datetime
        self.assertTrue(hasattr(test_model, 'updated_at'))
        self.assertIsNotNone(test_model.updated_at)
        self.assertIsInstance(test_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
