#!/usr/bin/python3
"""
Contains unittests for models/city.py.
"""

import os
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage

class TestCityDocs(unittest.TestCase):
    """Tests documentation and style of City class."""
    
    @classmethod
    def setUpClass(cls):
        """Set up for doc tests."""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test PEP8 conformity in models/city.py."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style issues found.")

    # ... (repeat for other test methods)

    def test_city_module_docstring(self):
        """Test city.py module docstring."""
        self.assertIsNot(city.__doc__, None, "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1, "city.py needs a docstring")

    # ... (repeat for other docstring tests)

class TestCity(unittest.TestCase):
    """Test the City class."""
    
    def test_is_subclass(self):
        """Test City is a subclass of BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    # ... (repeat for other test methods)

    def test_str(self):
        """Test that the str method has the correct output."""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))

if __name__ == "__main__":
    unittest.main()

