#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None

    len_of_my_list = len(my_list) - 1

    if idx > len_of_my_list:
        return None

    return my_list[idx]
