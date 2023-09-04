#!/usr/bin/python3
""" Module for a rectangle """


class Rectangle:
    """
    Empty rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        class instantiator

        Args:
            Self : Argv0
            width: width arg. 0
            height: height arg. 0

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        Args:
            self
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        Args:
            self: self
            value: value to set as width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        Args:
            self
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        Args:
            self: self
            value: value to set as height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value