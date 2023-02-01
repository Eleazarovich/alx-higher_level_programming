#!/usr/bin/python3
"""
4-print_square.py module

the module cointains one function, print_square(size)
"""


def print_square(size):
    """prints a square with the character #"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print("#" * size)
