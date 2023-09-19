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
        """
        setter for size attribute
        """
        self.valid_attribute(size, "width")
        self.width = size
        self.height = size

    def __str__(self):
        """returns formated rep of object"""
        return(f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """
        Update square args
        Args:
            args if args are used in order
            kwargs is kwargs are used key:value
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Convert obj member to script
        """
        dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return dict
