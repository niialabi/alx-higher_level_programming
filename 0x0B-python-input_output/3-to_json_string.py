#!/usr/bin/python3
"""
Returns json rep of python object
"""
import json


def to_json_string(my_obj):
    """
    function encodes obj to json spec

    Args:
        my_obj: Oject parsed
    """
    return json.dumps(my_obj)
