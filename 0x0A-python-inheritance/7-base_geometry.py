#!/usr/bin/python3
'''Base geometry'''


class BaseGeometry():
    '''Empty class'''
    def area(self):
        '''Exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
