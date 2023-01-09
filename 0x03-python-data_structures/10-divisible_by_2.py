#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return

    new_list = list()

    for i in my_list:
        new_list.append(True) if i % 2 == 0 else new_list.append(False)

    return new_list
