#!/usr/bin/python3

def add_integer(a, b=98):
    """ Function that adds 2 ints/floats
    
    Final output will be typeset to an int

    Args:
        a (int/float): First Arg. to be added
        b (int/float): Second Arg. to be added
        
    Returns:
        Int value of sum of a & b

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
