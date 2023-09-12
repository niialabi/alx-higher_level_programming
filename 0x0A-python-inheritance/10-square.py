#!/usr/bin/python3
"""
Module containing square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square sub class
    """
    def __init__(self, size):
        """
        Instantiating square class
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
