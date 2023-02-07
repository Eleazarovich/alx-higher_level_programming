#!/usr/bin/python3
"""
9-rectangle.py module

the module is based on 8-rectangle.py
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns a rectangle description"""
        return f"[{Rectangle.__name__}] {self.__width}/{self.__height}"
