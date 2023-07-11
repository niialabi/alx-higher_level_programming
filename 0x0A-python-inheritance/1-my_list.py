#!/usr/bin/python3
"""
Module that creates a class
that inherits from list
"""


class MyList(list):
    """
    Class that inherits from list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
