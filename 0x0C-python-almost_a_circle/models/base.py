#!/usr/bin/python3
"""
Module containing Base Class
"""

import json


class Base:
    """
    Base Class in almost circle project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for base class
        Args:
            id(optional): self selected id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        converts list of dictionaries
        Args:
            list_dictionaries: dict list
        """
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return ("[]")
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        json to string file function
        """
        obj_list = []
        if list_objs:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(Base.to_json_string(obj_list if obj_list else []))
