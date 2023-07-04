#!/usr/bin/python3
""" Module to print square with # character """

def print_square(size):
    """
    Function that prints square of size (size)
    
    Args:
        size: size of square

    Returns:
        Square of size size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    for x in range(size):
        for x in range(size):
            print("#", end= "")
        print()
