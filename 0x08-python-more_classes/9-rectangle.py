#!/usr/bin/python3
"""
9-rectangle.py module

the module defines a rectangle based on 8-rectangle.py
"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

    def __str__(self):
        """string representation of a triagle"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        s = self.print_symbol

        rect = "\n".join(str(s) * self.__width for _ in range(self.__height))

        return rect

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
