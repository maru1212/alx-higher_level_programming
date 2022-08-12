#!/usr/bin/python3
""" A new square class which inherits form rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A new class called square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new square.
        Args:
            size (int): The size of the new square.
            x (int): the x coordinate of the new square.
            y (int): the y coordinate of the new square.
            id (int): the identity of the new square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return("{} ({}) {}/{} - {}".format(__class__.__name__, self.id,
                                           self.x, self.y, self.size))
