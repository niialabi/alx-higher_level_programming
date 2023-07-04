#!/usr/bin/python3
""" Module prints out name <first name> <last name> """

def say_my_name(first_name, last_name=""):
    """
    Function prints out first name last name
    

    Args:
        first_name: First name arg
        last_name: Last name arg
        
    Returns:
        My name is <first name> <last name>

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
