#!/usr/bin/python3
"""
Contains unittests for models/review.py.
"""

import os
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage

class TestReviewDocs(unittest.TestCase):
    """Tests documentation and style of Review class."""
    
    @classmethod
    def setUpClass(cls):
        """Set up for doc tests."""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test PEP8 conformity in models/review.py."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style issues found.")

    # ... (repeat for other test methods)

    def test_review_module_docstring(self):
        """Test review.py module docstring."""
        self.assertIsNot(review.__doc__, None, "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1, "review.py needs a docstring")

    # ... (repeat for other docstring tests)

class TestReview(unittest.TestCase):
    """Test the Review class."""
    
    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    # ... (repeat for other test methods)

    def test_str(self):
        """Test that the str method has the correct output."""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

if __name__ == "__main__":
    unittest.main()

