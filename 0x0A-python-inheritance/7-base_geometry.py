#!/usr/bin/python3
"""
Geometry Class
"""


class BaseGeometry:
    """
    Class is empty
    """

    def area(self):
        """
        area method of Geometry class
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Int validator method

        Args:
            name: name of value
            value: value to validate
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
