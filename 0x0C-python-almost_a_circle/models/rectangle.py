#!/usr/bin/python3
"""
Module containing Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        Args:
            width: width
            height: height
            x: optional x-axis
            y: optional y-axis
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for with of rectangle value
        """
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width"""
        self.valid_attribute(width, "width")
        self.__width = width

    @property
    def height(self):
        """
        getter for rect. height val
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter for height
        """
        self.valid_attribute(height, "height")
        self.__height = height

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter for x
        """
        self.valid_attribute(x, "x")
        self.__x = x

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter for y
        """
        self.valid_attribute(y, "y")
        self.__y = y

    def valid_attribute(self, value, value_name):
        """
        value: val to be set
        value_name: dfdi
        """
        if not isinstance(value, int):
            raise TypeError(value_name + " must be an integer")
        if value_name == "width" or value_name == "height":
            if value < 1:
                raise ValueError(value_name + " must be > 0")
        if value_name == "x" or value_name == "y":
            if value < 0:
                raise ValueError(value_name + " must be >= 0")

    def area(self):
        """
        function that conputes area of rectangle
        """
        return (self.width * self.height)

    def display(self):
        """
        function that displays rectangle as #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for x in range(self.width):
                if x == (self.width - 1):
                    print("#")
                else:
                    print("#", end="")

    """def __str__(self):
        return ("[" + type(self).__name__ + "] " +
                str(self.__width) + "/" + str(self.__height))
    """

    def __str__(self):
        """
        returns str rep of object
        """
        return (f"[{type(self).__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        updates objec mutiple arguments
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns string rep of obj
        """
        dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dict
