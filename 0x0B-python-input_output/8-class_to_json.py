#!/usr/bin/python3
"""
Module for func class_to_json
"""
def class_to_json(obj):
    """
    Function return dictionary description of obj
    """
    return obj.__dict__
