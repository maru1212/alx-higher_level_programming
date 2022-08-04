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

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the area of the new rectangle. """

        return self.__width * self.__height

    def __str__(self):
        """ Returns with the string print statement. """

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)

        return string
