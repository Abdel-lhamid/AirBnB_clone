#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Remove the file if it exists to start with a clean slate
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up any remaining files after each test
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_file_path_exists(self):
        # Check if __file_path attribute exists
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_file_path_initial_value(self):
        # Check if __file_path attribute has the correct initial value
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_file_path_file_exists(self):
        # Check if the file exists after initializing FileStorage
        self.assertTrue(os.path.exists("file.json"))

    def test_objects_initial_value(self):
        # Check if __objects attribute exists and is initially empty
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertEqual(len(self.storage.all()), 0)

    def test_all_method(self):
        # Check if the all() method returns the __objects dictionary
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new_method(self):
        # Check if the new() method correctly adds objects to __objects
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_save_method(self):
        # Check if the save() method correctly serializes objects to JSON file
        obj = BaseModel()
        obj.name = "Test"
        obj.save()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method(self):
        # Check if the reload() method correctly deserializes objects from JSON file
        obj = BaseModel()
        obj.name = "Test"
        obj.save()
        self.storage.new(obj)
        self.storage.save()

        # Create a new FileStorage instance to ensure reloading
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 1)


if __name__ == '__main__':
    unittest.main()
