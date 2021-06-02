#!/usr/bin/python3
'''Rectangle inherits from BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class'''
    def __init__(self, width, height):
        '''Initializes the rectangle'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''return area of the rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''return rectangle'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
