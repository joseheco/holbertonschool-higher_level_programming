#!/usr/bin/python3
'''Square'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Square'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''string of square'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
