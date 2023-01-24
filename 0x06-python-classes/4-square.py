#!/usr/bin/python3
"""class `Square` that defines a square by:
    (based on 3-square.py)
"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size ** 2)
