#!/usr/bin/python3
'''Write class Student'''


class Student:
    '''class student'''
    def __init__(self, first_name, last_name, age):
        '''information'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''dictionary'''
        return self.___dict__
