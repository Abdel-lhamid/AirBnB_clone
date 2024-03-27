#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def test_instance_creation(self):
        # Test if we can create an instance of Place
        place = Place()
        self.assertIsInstance(place, Place)

    def test_inheritance(self):
        # Test if Place class inherits from BaseModel
        self.assertTrue(issubclass(Place, BaseModel))

    def test_city_id(self):
        # Test if Place class has a city_id attribute
        self.assertTrue(hasattr(Place, 'city_id'))

    def test_user_id(self):
        # Test if Place class has a user_id attribute
        self.assertTrue(hasattr(Place, 'user_id'))

    def test_name(self):
        # Test if Place class has a name attribute
        self.assertTrue(hasattr(Place, 'name'))

    # Add more attribute tests as needed

if __name__ == '__main__':
    unittest.main()
