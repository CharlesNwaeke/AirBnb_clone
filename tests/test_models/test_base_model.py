#!/usr/bin/python3
"""Tests the basemodels"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """tests for basemodel"""
    @classmethod
    def setUpClass(cls):
        """sets up"""
        cls.testBase = BaseModel()
        cls.testBase.x = "x"
        cls.testBase.y = 100

    @classmethod
    def tearDownClass(cls):
        """tears down"""
        del cls.testBase
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_basemodel(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings_basemodel(self):
        self.assertTrue(len(BaseModel.__doc__) > 0)
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

    def test_functions_basemodel(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(self.testBase.created_at == self.testBase.updated_at)

    def test_init_basemodel(self):
        self.assertTrue(isinstance(self.testBase, BaseModel))

    def test_save_basemodel(self):
        self.testBase.save()
        self.assertNotEqual(self.testBase.created_at, self.testBase.updated_at)

    def test_to_dict_basemodel(self):
        copy = self.testBase.to_dict()
        self.assertEqual(self.testBase.__class__.__name__, "BaseModel")
        self.assertIsInstance(copy['created_at'], str)
        self.assertIsInstance(copy['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
