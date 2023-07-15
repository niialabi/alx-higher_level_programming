#!/usr/bin/python3
"""
Module function that returns True if the object is an
"""


def inherits_from(obj, a_class):
    """
    Function checks if instance of inherited class

    Args:
        Obj: Object
        a_class: class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
