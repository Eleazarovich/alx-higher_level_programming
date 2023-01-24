#!/usr/bin/python3
"""class `Square that defines a square by:
    (based on 1-square.py)
"""


class Square:
    """difines a `Square`
    * Private instances attribute: 'size'
    * Instantiaion with optional 'size': def __init__(self, size=0):
        * 'size' must be an iteger, otherwise raise a TypeError
        * if 'size' is less than 0, raise ValueError
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
