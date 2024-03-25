#!/usr/bin/python3
import os
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A class for testing edge cases of the BaseModel class"""

    def test_empty_init(self):
        """Test creating an instance with no arguments"""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.id, str)

    def test_init_with_arguments(self):
        """Test creating an instance with arguments"""
        obj = BaseModel(id="test_id", created_at="2024-01-01T00:00:00.000000",
                        updated_at="2024-01-01T00:00:00.000000")
        self.assertEqual(obj.id, "test_id")
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def test_invalid_datetime_format(self):
        """Test creating an instance with invalid datetime format"""
        with self.assertRaises(ValueError):
            BaseModel(created_at="2024-01-01 00:00:00.000000",
                      updated_at="2024-01-01 00:00:00.000000")

    def test_invalid_attribute_name(self):
        """Test creating an instance with invalid attribute name"""
        obj = BaseModel()
        with self.assertRaises(AttributeError):
            obj.invalid_attribute = "value"

    def test_invalid_attribute_type(self):
        """Test creating an instance with invalid attribute type"""
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.id = 123

    def test_save_method(self):
        """Test the save method"""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        obj = BaseModel(id="test_id", created_at="2024-01-01T00:00:00.000000",
                        updated_at="2024-01-01T00:00:00.000000")
        expected_dict = {'id': 'test_id', 'created_at': '2024-01-01T00:00:00.000000',
                         'updated_at': '2024-01-01T00:00:00.000000', '__class__': 'BaseModel'}
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_str_representation(self):
        """Test the __str__ method"""
        obj = BaseModel(id="test_id", created_at="2024-01-01T00:00:00.000000",
                        updated_at="2024-01-01T00:00:00.000000")
        expected_str = "[BaseModel] (test_id) {'id': 'test_id', 'created_at': " \
                       "'2024-01-01T00:00:00.000000', 'updated_at': '2024-01-01T00:00:00.000000'}"
        self.assertEqual(str(obj), expected_str)

    def test_new_instance_from_dict(self):
        """Test creating a new instance from a dictionary"""
        data = {'id': 'test_id', 'created_at': '2024-01-01T00:00:00.000000',
                'updated_at': '2024-01-01T00:00:00.000000', '__class__': 'BaseModel'}
        obj = BaseModel(**data)
        self.assertEqual(obj.id, 'test_id')
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def test_new_instance_from_empty_dict(self):
        """Test creating a new instance from an empty dictionary"""
        obj = BaseModel(**{})
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.id, str)


if __name__ == '__main__':
    unittest.main()

