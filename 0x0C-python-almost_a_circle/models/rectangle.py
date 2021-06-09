#!/usr/bin/python3
'''First Rectangle'''


from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Rectangle'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width'''
        return self.__width

    @property
    def height(self):
        '''width'''
        return self.__height

    @property
    def x(self):
        '''x'''
        return self.__x

    @property
    def y(self):
        '''y'''
        return self.__y
