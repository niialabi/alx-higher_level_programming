#!/usr/bin/python3
"""
Module prints pascal triangle given (n)
"""


def pascal_triangle(n):
    """
    prints pascal's triangle

    Args:
        n: number
    """
    if n < 1:
        return []
    
    for i in range(n):
        print(" "*(n-i), end="")
        print(" ".join(map(str, str(11**i))))
