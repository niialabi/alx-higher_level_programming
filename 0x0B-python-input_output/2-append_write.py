#!/usr/bin/python3
"""
Module that appends text to file or creates new file
"""

def append_write(filename="", text=""):
    """
    function appends text to file
    
    Args:
        filename: path of file
        text: string to append
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
