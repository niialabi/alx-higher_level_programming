#!/usr/bin/python3
"""
Module that writes string to file
"""


def write_file(filename="", text=""):
    """
    Function writes txt to file

    Args:
        filename: location and filename
        tex: text content
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(text)
