#!/usr/bin/python3
"""
Module decodes json
"""
import json


def from_json_string(my_str):
    """
    Function decodes json str to py obj

    Args:
        my_string: json str
    """

    return json.loads(my_str)
