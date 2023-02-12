#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """rectangle class (inherits from Base)"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets passed value to the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets passed value to the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the x co-ordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the passed value to the x co-ordinate"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the y co-ordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets passed value to the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Reactangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle to stdout using character #"""
        print('\n' * self.y + '\n'.join([' ' * self.x +
                                         '#' * self.width
                                         for i in range(self.height)]))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attributes = ["id", "width", "height", "x", "y"]
        for i, j in zip(attributes, args):
            setattr(self, i, j)
        for i, j in kwargs.items():
            setattr(self, i, j)

    def to_dictionary(self):
        """returns dictionary representaion of the rectangle"""
        attributes = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in attributes}

    def __str__(self):
        """string representation of the rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".\
                format(type(self).__name__, self.id, self.x, self.y,
                        self.width, self.height)
