#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_instance_creation(self):
        # Test if we can create an instance of State
        state = State()
        self.assertIsInstance(state, State)

    def test_inheritance(self):
        # Test if State class inherits from BaseModel
        self.assertTrue(issubclass(State, BaseModel))

    def test_name(self):
        # Test if State class has a name attribute
        self.assertTrue(hasattr(State, 'name'))

if __name__ == '__main__':
    unittest.main()
