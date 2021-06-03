#!/usr/bin/python3
'''Function JSON'''


import json


def save_to_json_file(my_obj, filename):
    '''JSON'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
