#!/usr/bin/python3
"""
2-is_same_class.py module

the module contains one function, is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class
    otherwise False
    """
    return type(obj) is a_class
