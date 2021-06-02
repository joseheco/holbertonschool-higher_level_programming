#!/usr/bin/python3
'''Rectangle inherits from BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class'''
    def __init__(self, width, height):
        '''Initializes the rectangle'''
        self.integer_validator(width)
        self.__width = width
        self.integer_validator(height)
        self.__height = height
