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

    def to_json(self):
        """
        method retireves a dictionary rep of student instance
        """
        return self.__dict__
