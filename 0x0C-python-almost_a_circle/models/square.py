#!/usr/bin/python3
"""
module contains square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter for size of square
        """
        return self.width

    @size.setter
    def size(self, size):
        self.valid_attribute(size, "width")
        self.width = size
        self.height = size

    def __str__(self):
        return(f"[{type(self).__name__}] {self.id} {self.x}/{self.y} - {self.width}")
