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

    @property
    def size(self):
        """
        Getter for class
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def area(self):
        """
        returns square area
        """
        return self._Square__size ** 2

    def my_print(self):
        """
        square printer
        """
    if _Square__size == 0:
            print()
        for a in range(self._Square__size):
            for a in range(self._Square__size):
                print("#", end='')
		print()
