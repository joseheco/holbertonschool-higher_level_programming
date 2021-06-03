#!/usr/bin/python3
'''Write File'''


def write_file(filename="", text=""):
    '''write_file'''
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
