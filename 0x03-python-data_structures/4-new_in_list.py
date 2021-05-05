#!/usr/bin/python3


def mew_in_list(my_list, idx, element):
    copy = []
    copy = my_list[:]
    if idx >= 0 and idx < len(my_list):
        copy[idx] = element
    return copy
