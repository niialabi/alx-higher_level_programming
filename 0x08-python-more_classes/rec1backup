#!/usr/bin/python3
"""
Empty rectanble module
"""


class Rectangle:
    """
    Empty rectangle class
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        width getter
        Args:
        self:
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
        self: self
        value: value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        Args:
            self:
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            self:
            value:
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        self.__height = value
