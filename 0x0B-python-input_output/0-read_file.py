#!/usr/bin/python3
"""
Module reads txt files and prints to stdout
"""


def read_file(filename=""):
    """
    Function reads file and printes to stdout

    Args:
        Filepath to file
    """
    with open(filename, mode="r", encoding="utf-8") as wrkfile:
        print(wrkfile.read(), end="")
