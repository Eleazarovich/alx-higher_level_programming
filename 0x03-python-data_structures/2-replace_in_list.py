#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None

    len_of_my_list = len(my_list) - 1

    if idx > len_of_my_list:
        return None

    my_list[idx] = element

    return my_list
