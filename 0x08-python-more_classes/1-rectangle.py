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
    """
    width getter
    Args:
        self
    """
    def width(self):
        return self.__width

    @width.setter
    """
    width setter
    Args:
        self: self
        value: value of new width
    """
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        self.__width = value
    

    @property
    """
    height getter 
    Args:
        self:
    """
    def height(self):
        return self.__height

    @height.setter
    """
    height setter
    Args:
        self:
        value:
    """
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        self.__height = value
