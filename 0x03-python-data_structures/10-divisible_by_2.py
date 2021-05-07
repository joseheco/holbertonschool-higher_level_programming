#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    resultado = []
    if my_list:
        for idx in range(0, len(my_list)):
            resultado.append(False if my_list[idx] % 2 else True)
    return resultado
