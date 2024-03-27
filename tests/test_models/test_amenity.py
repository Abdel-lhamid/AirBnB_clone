#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_instance_creation(self):
        # Test if we can create an instance of Amenity
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_inheritance(self):
        # Test if Amenity class inherits from BaseModel
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_name(self):
        # Test if Amenity class has a name attribute
        self.assertTrue(hasattr(Amenity, 'name'))

if __name__ == '__main__':
    unittest.main()
