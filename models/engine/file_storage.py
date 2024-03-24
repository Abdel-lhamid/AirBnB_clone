#!/usr/bin/python3
"""Module for FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from model.review import Review


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    attrs:
        __file_path
        __objects
    methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel,
               "User": User, "State": State,
               "City": City, "Amenity": Amenity,
               "Place": Place, "Review": Review}

    def all(self):
        """funtion that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
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
            for k, v in json_data.items():
                self.__objects[k] = self.classes[k.split('.')[0]](**v)
