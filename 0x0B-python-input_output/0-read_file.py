#!/usr/bin/python3
"""
Mdule containing read_file function
"""


def read_file(filename=""):
    """
    fuction that reads a txt fine & prints to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
