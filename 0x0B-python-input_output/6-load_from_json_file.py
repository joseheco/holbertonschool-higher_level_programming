#!/usr/bin/python3
'''function JSON'''


import json


def load_from_json_file(filename):
    '''JSON'''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f.read())
