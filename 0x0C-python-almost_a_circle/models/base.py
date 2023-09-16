#!/usr/bin/python3
"""Module containing Base Class"""


class Base:
    """
    Base Class in almost circle project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
