#!/usr/bin/python3
"""
Function if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Function to check if obj is instance of class

    Args:
        obj: object to check
        a_class: class to check against
    """
    return type(obj) == a_class
