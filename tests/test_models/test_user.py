#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def test_instance_creation(self):
        # Test if we can create an instance of User
        user = User()
        self.assertIsInstance(user, User)

    def test_inheritance(self):
        # Test if User class inherits from BaseModel
        self.assertTrue(issubclass(User, BaseModel))

    def test_email_attribute(self):
        # Test if User class has an email attribute
        self.assertTrue(hasattr(User, 'email'))

    def test_password_attribute(self):
        # Test if User class has a password attribute
        self.assertTrue(hasattr(User, 'password'))

    def test_first_name_attribute(self):
        # Test if User class has a first_name attribute
        self.assertTrue(hasattr(User, 'first_name'))

    def test_last_name_attribute(self):
        # Test if User class has a last_name attribute
        self.assertTrue(hasattr(User, 'last_name'))

    def test_email_validation(self):
        # Test if email attribute is a string
        user = User()
        user.email = "test@example.com"
        self.assertIsInstance(user.email, str)

    def test_password_validation(self):
        # Test if password attribute is a string
        user = User()
        user.password = "securepassword"
        self.assertIsInstance(user.password, str)

    def test_first_name_validation(self):
        # Test if first_name attribute is a string
        user = User()
        user.first_name = "John"
        self.assertIsInstance(user.first_name, str)

    def test_last_name_validation(self):
        # Test if last_name attribute is a string
        user = User()
        user.last_name = "Doe"
        self.assertIsInstance(user.last_name, str)

    def test_to_dict_method(self):
        # Test if to_dict() method returns dictionary representation of User instance
        user = User(email="test@example.com", password="securepassword", first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "securepassword")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")

    def test_str_representation(self):
        # Test if __str__() method returns the expected string representation
        user = User(email="test@example.com", password="securepassword", first_name="John", last_name="Doe")
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

if __name__ == '__main__':
    unittest.main()

