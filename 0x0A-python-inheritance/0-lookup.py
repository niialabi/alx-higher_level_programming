#!/usr/bin/python3
"""
Module that contains lookup function
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an obj
    """
    return dir(obj)
