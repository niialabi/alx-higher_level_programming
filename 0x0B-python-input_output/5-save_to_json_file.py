#!/usr/bin/python3
"""
Function module that saves obj to file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function saves obj to file
    
    Args:
        my_obj: Object

        filename: file to write to
    """
    with open(filename, mode="w") as f:
        return f.write(json.dumps(my_obj))
