#!/usr/bin/python3
"""A base class"""
import json


class Base:
    """ A base class
        Private Class Attributes:
            __nb_objects (int): Number of instantiated Bases.
        """

    __nb_objects = 0

    def __init__(self, id=None):
        """Intiator
        Args:
            id(int): unique id of an object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A static method which converts dictionary to json str. """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
