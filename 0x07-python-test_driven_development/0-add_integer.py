#!/usr/bin/python3
"""
0-add_integer module

the module provides one function, add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    add_integer adds two integers

    Args:
        a: first integer
        b: second integer, default 98

    Raises:
        TypeError: if a or b are not integers or floats

    Returns:
        the sum of a and b
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
