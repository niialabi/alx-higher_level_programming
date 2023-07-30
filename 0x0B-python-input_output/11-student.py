#!/usr/bin/python3
"""
Module contains student class
"""


class Student:
    """
    Class name: Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instatiation self

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
        method retireves a dictionary rep of student instance
        """
        diction = {}
        if type(attrs) is list:
            for element in attrs:
                if type(element) is not str:
                    break
                if hasattr(self, element):
                    diction[element] = getattr(self, element)
            return diction

        return self.__dict__

    def reload_from_json(self, json):
        """
        Instance that will replace all attributes
        of the Student instance
        """
        for key in json:
            setattr(self, key, json[key])
