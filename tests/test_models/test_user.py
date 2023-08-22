#!/usr/bin/python3
"""
Contains unittests for models/state.py.
"""

import os
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage

class TestStateDocs(unittest.TestCase):
    """Tests documentation and style of State class."""
    
    @classmethod
    def setUpClass(cls):
        """Set up for doc tests."""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Test PEP8 conformity in models/state.py."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style issues found.")

    # ... (repeat for other test methods)

    def test_state_module_docstring(self):
        """Test state.py module docstring."""
        self.assertIsNot(state.__doc__, None, "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1, "state.py needs a docstring")

    # ... (repeat for other docstring tests)

class TestState(unittest.TestCase):
    """Test the State class."""
    
    def test_is_subclass(self):
        """Test if State is a subclass of BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    # ... (repeat for other test methods)

    def test_str(self):
        """Test that the str method has the correct output."""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))

if __name__ == "__main__":
    unittest.main()

