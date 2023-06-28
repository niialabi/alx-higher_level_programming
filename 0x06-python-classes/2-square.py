#!/usr/bin/python3
"""
Module
create class square
"""


class Square:
    """
    class name: square
    """
    def __init__(self, size=0):
        """
        Private instance of size
        raise value erro && type error

        Args:
        size of type int
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """
            privage obj(size) of square class
            """
            self._Square__size = size
