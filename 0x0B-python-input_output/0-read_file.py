#!/usr/bin/python3
'''Read File'''


def read_file(filename=""):
    '''Read text file'''
    with open(filename, 'r', encoding='utf8') as f:
        print (f.readline())
