#!/usr/bin/python3
'''Base models'''


import json


class Base:
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Base'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''JSON string dictionaries'''
