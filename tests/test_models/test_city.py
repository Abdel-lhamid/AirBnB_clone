#!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_instance_creation(self):
        # Test if we can create an instance of City
        city = City()
        self.assertIsInstance(city, City)

    def test_inheritance(self):
        # Test if City class inherits from BaseModel
        self.assertTrue(issubclass(City, BaseModel))

    def test_state_id(self):
        # Test if City class has a state_id attribute
        self.assertTrue(hasattr(City, 'state_id'))

    def test_name(self):
        # Test if City class has a name attribute
        self.assertTrue(hasattr(City, 'name'))

if __name__ == '__main__':
    unittest.main()
