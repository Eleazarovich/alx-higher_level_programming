#!/usr/bin/python3
"""
2-rectangle.py module

the module defines a rectangle based on 1-rectangle.py
"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """retrives the height as a private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value to the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """retrives the width as a private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value to the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
