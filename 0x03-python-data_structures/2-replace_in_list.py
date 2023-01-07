#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len_of_my_list = len(my_list) - 1

    if idx > len_of_my_list or idx < 0:
        return my_list

    my_list[idx] = element

    return my_list
