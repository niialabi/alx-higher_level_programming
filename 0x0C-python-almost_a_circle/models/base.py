#!/usr/bin/python3
"""
Module is base of all other classes in this project
"""


class Base:
    """
    Base class for all project classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiationg Base

        Args:
            id: id(optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that returns the JSON string representation of
        """
        if len(list_dictionaries) < 1
            return "[]"
        return json.dumps(list_dictionaries)
