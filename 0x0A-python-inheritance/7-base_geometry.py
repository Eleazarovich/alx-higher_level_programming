#!/usr/bin/python3
"""
7-base_geometry.py module

the module contains one class, based on 6-base_geometry.py
"""


class BaseGeometry:
    """class BaseGeometry"""
    def __init__(self):
        """new instance of BaseGeometry"""
        pass

    def area(self):
        """raises an exception if area is not implemeted"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if the value is an integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
