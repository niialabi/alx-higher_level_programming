#!/usr/bin/python3
"""
Write a function that returns True if
the object is an instance of, or if
the object is an instance of a class
that inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Function ret true if instance of ...
    or false
    """
    return isinstance(obj, a_class)
