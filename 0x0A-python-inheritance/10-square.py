#!/usr/bin/python3
""" Author: Maranata, A new class Square. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A new class called Sqaure. """

    def __init__(self, size):
        """ Instantiation with an attribute called size.

        Args:
            Size(int): The size of the new Square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
