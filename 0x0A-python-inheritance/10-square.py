#!/usr/bin/python3
'''Class Square inherits from rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size):
        '''sizes the square'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''area square'''
        return self.__size ** 2
