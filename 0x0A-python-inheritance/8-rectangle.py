#!/usr/bin/python3
""" Author: Maranata Feleke, an emtpy class. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is an empty class. """

    def __init__(self, width, height):
        """ Instantiation of the attriibutes.

        Args:
             width(int): width of the rectangle.
             height(int): height of the rectangle.
        """

        self._width = width
        self._height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
