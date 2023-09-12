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
        self.__height = heighti
