#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = dict()
    for k, v in a_dictionary.items():
        n_dictionary[k] = v * 2

    return n_dictionary
