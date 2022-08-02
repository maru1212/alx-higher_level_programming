#!/usr/bin/python3
""" Author: Maranata Feleke, an emtpy class. """


class BaseGeometry:
    """ This is an empty class. """

    def area(self):
        """ A function which raises an exception."""
        raise Exception("area() is not implemebted")

    def integer_validator(self, name, value):
        """ A function which validats an integer.

        Args:
             name(str): The name of the parameter.
             value(int): The parameter to validate.
        Raises:
             TypeError: If value is not integer.
              ValueError: IF value is <= 0.
        """

        if not isinstance(type(value), int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
