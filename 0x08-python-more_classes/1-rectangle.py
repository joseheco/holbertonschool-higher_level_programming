#!/usr/bin/python3
"""Define rectangle"""

class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        """Init rectangle"""
        self.width = width
        self.height = height

    @property
    """Private Attributes"""
    def width(self):
        return self.__width

    @width.setter
    """Privte Attributes"""
    def width(self, value):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    """Private Attributes"""
    def height(self):
        return self.__height

    @height.setter
    """Private Attributes"""
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
