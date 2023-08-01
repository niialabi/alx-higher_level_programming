#!/usr/bin/python3
"""
Module is base of all other classes in this project
"""

import json


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
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves list of object to json file
        """
        list_j = []
        if list_objs:
            for element in list_objs:
                list_j.append(cls.to_dictionary(element))
        with open("{}.json", format(cls.__name__), "W") as file:
            file.write(Base.to_json_string(json_list))
        
