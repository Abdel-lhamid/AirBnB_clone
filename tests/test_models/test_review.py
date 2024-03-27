#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_instance_creation(self):
        # Test if we can create an instance of Review
        review = Review()
        self.assertIsInstance(review, Review)

    def test_inheritance(self):
        # Test if Review class inherits from BaseModel
        self.assertTrue(issubclass(Review, BaseModel))

    def test_place_id(self):
        # Test if Review class has a place_id attribute
        self.assertTrue(hasattr(Review, 'place_id'))

    def test_user_id(self):
        # Test if Review class has a user_id attribute
        self.assertTrue(hasattr(Review, 'user_id'))

    def test_text(self):
        # Test if Review class has a text attribute
        self.assertTrue(hasattr(Review, 'text'))

if __name__ == '__main__':
    unittest.main()
