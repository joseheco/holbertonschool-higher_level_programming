#!/usr/bin/python3
'''Sub class'''


def inherits_from(obj, a_class):
    '''Function return True if its inherit_from
    , otherwise False'''
    return issubclass(type(obj), a_class) and (type(obj) != a_class)
