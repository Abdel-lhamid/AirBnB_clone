#!/usr/bin/python3
"""Module for FileStorage class"""
import json
import os


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """funtion that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data_to_save = {}
        for k, v in self.__objects.items():
            data_to_save[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(data_to_save, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists, otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, 'r') as f:
            json_data = json.load(f)
