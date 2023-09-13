#!/usr/bin/python3
"""
module contains write file function
"""


def write_file(filename="", text=""):
    """
    function writes string to text file
    
    Args:
    filename: creates one if not found

    text: string to be written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text);
