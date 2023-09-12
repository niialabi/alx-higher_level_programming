#!/usr/bin/python3
"""
Module Rectanclge contains class Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle Class building
    """
    def __init__(self, width, height):
        """
        Instantiation of width and height

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Area method that returns area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        properly formated output when print obj
        """
        return ("[" + type(self).__name__ + "] " +
                str(self.__width) + "/" + str(self.__height))
