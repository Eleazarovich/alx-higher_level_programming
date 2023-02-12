#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """assings size to the height and width"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square"""
        attributes = ["id", "size", "x", "y"]
        for i, j in zip(attributes, args):
            setattr(self, i, j)
        for i, j in kwargs.items():
            setattr(self, i, j)

    def to_dictionary(self):
        """returns dictionary representaion of a square"""
        attributes = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in attributes}

    def __str__(self):
        """string representation of the square"""
        return "[{}] ({}) {}/{} - {}".\
                format(type(self).__name__, self.id, self.x, self.y, self.size)
