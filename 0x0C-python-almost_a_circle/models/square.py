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

    def update(self, *args, **kwargs):
        """update the new square.
        Args:
            args (int):
                - 1st argument should be the id attribute.
                - 2nd argument should be the size attribute.
                - 3rd argument should be the x attribute.
                - 4th argument should be the y attribute.
            kwargs(key & value): includes a key and value for it.
        """
        if args and len(args) != 0:
            inc = 0
            for argument in args:
                if inc == 0:
                    if args is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = argument
                elif inc == 1:
                    self.size = argument
                elif inc == 2:
                    self.x = argument
                elif inc == 3:
                    self.y = argument
                inc += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
