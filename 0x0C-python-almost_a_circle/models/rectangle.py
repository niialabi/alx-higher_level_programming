#!/usr/bin/python3
"""
Rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiating Rectangle obj.

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int, optional): x coordinate of rect
            y (int, optional); y coordinate of rect
            id (int, optional): id of rect
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Returns width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets value to width of rectangle
        """
        self.value_check("width", width)
        self.__width = width

    @property
    def height(self):
        """
        Returns height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets value to height of rectangle
        """
        self.value_check("height", height)
        self.__height = height

    @property
    def x(self):
        """
        Returns x value of rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets value to x coordinate of rectangle
        """
        self.value_check("x", x)
        self.__x = x

    @property
    def y(self):
        """
        Returns y value of rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets value to y coordinate of rectangle
        """
        self.value_check("y", y)
        self.__y = y

    def value_check(self, name, value):
        """
        Checks the value for atributes

        Args:
            name (str): The name of the attribute being validated.
            value: The value to be validated.

        Raise:
            TypeError: If the value is not an integer.
            ValueError: If the value is less or equal to 0 for
                    "width" or "height", or less than 0 for "x" or "y".
        """
        if value is not None and type(value) is not int:
            raise TypeError(name + " must be an integer")
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(name + " must be > 0")
        if (name == "y" or name == "x") and value < 0:
            raise ValueError(name + " must be >= 0")

    def area(self):
        """
        Area method for Rectangle class
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout Rectangle instance with #
        """
        for x in range(self.height):
            for y in range(self.width):
                print("#", end="")
            print()