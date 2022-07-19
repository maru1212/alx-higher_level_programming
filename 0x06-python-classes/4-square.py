#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
             size(int): The size of the new square
        """
        self.__size = size
    @property
    def size(self):
        """Retriving size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting size."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """To find the area."""

    def area(self):
        """Find the area of a square."""

        return self.__size * self.__size
