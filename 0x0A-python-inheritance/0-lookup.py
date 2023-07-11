#!/usr/bin/python3
"""
function that returns the
list of available attributes
and methods of an object:
"""


def lookup(obj):
    """
    A function that returns the
    list of available attributes
    and methods of an object:

    Args:
        obj
    """
    return dir(obj)
