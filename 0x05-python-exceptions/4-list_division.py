#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    list_n = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[index] / my_list_2[index]
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            list_n.append(result)
            result = 0
        return list_n
