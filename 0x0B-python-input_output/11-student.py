#!/usr/bin/python3
"""
module containing student class
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiat self

        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method returns dic rep. of student
        """
        dict = {}
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    break
                if hasattr(self, item):
                    dict[item] = getattr(self, item)
            return dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        function replaceses all att. of
        student instance
        """
        for key_in_dict in json:
            setattr(self, key_in_dict, json[key_in_dict])
