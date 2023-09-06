#!/usr/bin/python3
"""
module containing locked class
"""


class LockedClass:
    """
    lockedclass class
    """
    def __setattr__(self, name, value):
        if name == 'first_name':
            # Allow creating the 'first_name' attribute
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'{type(self).__name__}'
                                 object has no attribute '{name}'")
