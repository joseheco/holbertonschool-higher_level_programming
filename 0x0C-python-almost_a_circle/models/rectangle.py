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
        return (self.__width)

    @property
    def height(self):
        '''width'''
        return (self.__height)

    @property
    def x(self):
        '''x'''
        return (self.__x)

    @property
    def y(self):
        '''y'''
        return (self.__y)

    @height.setter
    def height(self, value):
        '''height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        '''width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        '''x.'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        '''y.'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''return area'''
        return(self.__width * self.__height)

    def __str__(self):
        '''str_self'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def uodate(self, *args):
        '''args Attributes'''
        if len(args):
            for i, ar in enumerate(args):
                if i == 0:
                    self.id = ar
                elif i == 1:
                    self.width = ar
                elif i == 2:
                    self.height = ar
                elif i == 3:
                    self.x = ar
                elif i == 4:
                    self.y = ar
