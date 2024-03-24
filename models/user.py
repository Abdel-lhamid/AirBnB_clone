#!/usr/bin/python3
""""
Module User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class that inherites from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
