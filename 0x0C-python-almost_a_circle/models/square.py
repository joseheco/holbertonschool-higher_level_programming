#!/usr/bin/python3
'''Square class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Square classt'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String of square'''
        return("[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width))

    @property
    def size(self):
        """size self"""
        return self.width

    @size.setter
    def size(self, value):
        """size self"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """argument attributes"""
        if args and len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary of a Square"""
        dicti = {}
        dicti["id"] = self.id
        dicti["size"] = self.size
        dicti["x"] = self.x
        dicti["y"] = self.y
        return dicti
