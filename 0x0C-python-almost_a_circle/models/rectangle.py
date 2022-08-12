#!/usr/bin/python3
""" A class called rectangle which inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """A class named Rectangle which inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer which includes attributes.
        Args:
            width(int): the width of the rectangle.
            height (int): the height of the rectangle.
            x (int): x attr.
            y (int): y attr.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """A function which returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle using the '#' character."""
        if self.__width == 0 or self.__height == 0:
            print("")
            return ()

        [print("") for m in range(self.y)]
        for i in range(self.__height):
            [print(" ", end="") for n in range(self.x)]
            [print("#", end="") for j in range(self.__width)]
            print("")

    def __str__(self):
        """A string initiater which returns a string."""
        return ("[{}] ({}) {}/{} - {}/{}".format(__class__.__name__, self.id,
                                                 self.x, self.y, self.width,
                                                 self.height))

    def update(self, *args):
        """Update the arguments of the rectangle.
        Args:
            *args (int): the new arguments.
                - 1st argument is the id attribute.
                - 2nd argument is the width attribute.
                - 3rd argument is the height attribute.
                - 4th argument is the x attribute.
                - 5th argument is the y attribute.
        """
        if args and len(args) != 0:
            inc = 0
            for argument in args:
                if inc == 0:
                    if argument is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = argument
                elif inc == 1:
                    self.width = argument
                elif inc == 2:
                    self.height = argument
                elif inc == 3:
                    self.x = argument
                elif inc == 4:
                    self.y = argument
                inc += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
