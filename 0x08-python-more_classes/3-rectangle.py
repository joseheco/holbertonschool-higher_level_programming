#!/usr/bin/python3
"""Define rectangle"""


class Rectangle:
    """Class
    rectangle"""

    def __init__(self, width=0, height=0):
        """Init rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private Attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """Private Attributes"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Private Attributes"""
        return self.__height

    @height.setter
    def height(self, value):
        """Private Attributes"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area"""
        return self.__width * self.__height

    def perimeter(self):
        """Area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Empty string"""
        if self.__width == 0 or self.__height == 0:
            string = ""
        else:
            for a in range(self.height):
                for b in range(self.width):
                    string += "#"
                if (a != (self.height -1)):
                    string += "\n"
        return string
