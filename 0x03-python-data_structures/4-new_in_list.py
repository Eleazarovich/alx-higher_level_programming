#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_of_my_list = len(my_list) - 1

    if idx < 0 or idx > len_of_my_list:
        return my_list

    copy_of_my_list = my_list[:]
    copy_of_my_list[idx] = element

    return copy_of_my_list
