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
        """A function which desplays the rectange with # format."""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        for i in range(self.__width):
            for j in range(self.__height):
                print("#", end= "")
            print("")
