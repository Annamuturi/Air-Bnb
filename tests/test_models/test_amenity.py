#!/usr/bin/python3
"""
Contains the TestAmenityDocs and TestAmenity classes
"""

import inspect
import pep8
import unittest
from models import amenity
from models.base_model import BaseModel

Amenity = amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """Tests documentation and style of Amenity class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors found.")

    # ... (other test methods)

    def test_amenity_func_docstrings(self):
        """Test presence of docstrings in Amenity methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""
    
    def test_is_subclass(self):
        """Test Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    # ... (other test methods)

    def test_str(self):
        """Test the str method output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

