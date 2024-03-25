#!/usr/bin/python3
""""
Module BaseModel class
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    BaseModel class:
    that defines all common attributes/methods for other classes
    Attributes:
        id, created_at, updated_at
    Methodes:
        __init__
        __str__
    """
    def __init__(self, *args, **kwargs):
        """ init constructor"""
        from models import storage
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    pass
                elif k == "updated_at" or k == "created_at":
                    setattr(self, k, datetime.
                            strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of BaseModel class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """update instance, update attr updated_at"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return a dictionary with all key/value"""
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        return _dict
