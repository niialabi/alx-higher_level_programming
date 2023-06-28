#!/usr/bin/python3
"""
Module
create class square
"""


class Square:
    """
    class name: square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Private instance of size
        raise value erro && type error

        Args:
            _Square__size (int): square size
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for class
        """
        return self.__size

    @property
    def position(self):
        """
        get position for c.square
        """
        return self.__position
	
    @position.setter
    def position(self, value):
        """
        set position for square class
        """
        if not isinstance(value, tuple) or len(value) != 2 or not isinstance(value[1], int) \
                or not isinstance(value[0], int) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """
        Setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        square printer
        """
        if self.__size == 0:
            return
        for a in range(self.__position[1]):
            print()
        for a in range(self.__size):
            for c in range(self.__position[0]):
                print(" ", end="")
            for d in range(self. __size):
                print("#", end="")
            print()
