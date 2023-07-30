#!/usr/bin/python3
"""
module for square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiating square object

        Args:
            size: size of square
            x (int): x optional
            y (int): y optional
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        line = "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width)
        return line

    @property
    def size(self):
        """
        Getter for size of quare
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter for size attr
        """
        self.value_check("width", size)
        self.width = size
        self.height = size
