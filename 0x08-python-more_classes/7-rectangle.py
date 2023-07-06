#!/usr/bin/python3
""" Module for a rectangle """


class Rectangle:
    """
    Empty rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        instance destructor
        Args:
            self: self
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """
        Area of a rectangle
        Args:
            self: self
        """
        return self.width * self.height

    def perimeter(self):
        """
        Perimeter of a rectangle
        Args:
            self:self
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height)*2

    def __str__(self):
        """
        prints rectangle with #
        Args:
            self: self
        """
        ret_string = ""
        if self.width == 0 or self.height == 0:
            return ret_string
        for i in range(self.height):
            for j in range(self.width):
                ret_string += str(self.print_symbol)
            if i != (self.height - 1):
                ret_string += "\n"
        return ret_string

    def __repr__(self):
        """
        string representation of the rectangle to \
        be able to recreate a new instance by using eval
        Args:
            self: self
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))
