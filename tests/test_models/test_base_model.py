#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import os
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Clean up test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass
        del cls.storage
        del cls.base

    def test_pep8(self):
        """Test PEP8 style."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "PEP8 style issues found.")

    def test_docstrings(self):
        """Test presence of docstrings."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        # ... (repeat for other methods)

    def test_attributes(self):
        """Test attributes."""
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_methods(self):
        """Test methods."""
        methods = ["__init__", "save", "to_dict", "delete", "__str__"]
        for method_name in methods:
            self.assertTrue(hasattr(BaseModel, method_name))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.base, BaseModel)

    # ... (repeat for other tests)

    def test_save(self):
        """Test save method."""
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertLess(old_updated_at, self.base.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("BaseModel.{}".format(self.base.id), f.read())

    def test_to_dict(self):
        """Test to_dict method."""
        base_dict = self.base.to_dict()
        self.assertEqual(type(base_dict), dict)
        self.assertEqual(self.base.id, base_dict["id"])
        self.assertEqual("BaseModel", base_dict["__class__"])
        self.assertEqual(self.base.created_at.isoformat(), base_dict["created_at"])
        self.assertEqual(self.base.updated_at.isoformat(), base_dict["updated_at"])
        self.assertNotIn("_sa_instance_state", base_dict)

    def test_delete(self):
        """Test delete method."""
        self.base.delete()
        self.assertNotIn(self.base, FileStorage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()

