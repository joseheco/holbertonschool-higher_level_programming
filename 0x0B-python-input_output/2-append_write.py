#!/usr/bin/python3
'''Append file'''


def append_write(filename="", text=""):
    '''append_write'''
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
