#!/usr/bin/python3
"""
Function module that creates an obj from file
"""
import json


def load_from_json_file(filename):
    """
    Function saves obj to file

    Args:
        filename: file to write to
    """
    with open(filename) as f:
        return json.loads(f.read)
