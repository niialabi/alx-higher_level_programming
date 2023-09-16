#!/usr/bin/python3
"""Module containing Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width"""
        self.valid_attribute(width, "width")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height"""
        self.valid_attribute(height, "height")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        self.valid_attribute(x, "x")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        self.valid_attribute(y, "y")
        self.__y = y

    def valid_attribute(self, value, value_name):
        if not isinstance(value, int):
            raise TypeError(value_name + " must be an integer")
        if value_name == "width" or value_name == "height":
            if value < 1:
                raise ValueError(value_name + " must be > 0")
        if value_name == "x" or value_name == "y":
            if value < 0:
                raise ValueError(value_name + " must be >= 0")

    def area(self):
        return (self.width * self.height)

    def display(self):
        for i in range (self.height):
            for x in range (self.width):
                if x == (self.width - 1):
                    print("#")
                else:
                    print("#", end="")
