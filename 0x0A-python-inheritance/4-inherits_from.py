#!/usr/bin/python3
"""
Module function that returns True if the object is an
instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Function checks if instance of inherited class

    Args:
        Obj: Object
        a_class: class
    """
    return type(obj) != a_class and isinstance(obj, a_class)
