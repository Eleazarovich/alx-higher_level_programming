#!/usr/bin/python3
"""
6-rectangle.py module

the module defines a rectangle based on 5-rectangle.py
"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """instantiation with optional width and height"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """string representation of a triagle"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        rectangle = "\n".join("#" * self.__width for _ in range(self.__height))

        return rectangle

    def __repr__(self):
        """
        returns a string representation of the rectangle to be able to
        recreate a new instance by using eval
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        prints the message Bye rectangle... when an instance of a rectangle
        is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
