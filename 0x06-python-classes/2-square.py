#!/usr/bin/python3
"""Defines Square"""


class Square:
    """Class Square
    Attributes:
        __size (int): size of a side of the square"""
    def __init__(self, size=0):
        """Initializes the square's size
        Args:
            size (int): size of a side of the square"""
        if type(size) is not int:
            raise TypeError("size")
        elif size < 0:
            raise ValueError("size")
        else:
            self.__size = size
