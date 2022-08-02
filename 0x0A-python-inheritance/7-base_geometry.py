#!/usr/bin/python3
""" Author: Maranata Feleke, an emtpy class. """


class BaseGeometry:
    """ This is an empty class. """

    def area(self):
        """ A function which raises an exception."""
        raise Exception("area() is not implemebted")

    def integer_validator(self, name, value):
        """ A function which validats an integer. """

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
