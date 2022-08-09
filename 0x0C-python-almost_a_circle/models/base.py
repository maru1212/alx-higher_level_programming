#!/usr/bin/python3
"""A base class"""


class Base:
    """ A base class
       private Attribute:
           __nb_objects(int): private attribute.
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
