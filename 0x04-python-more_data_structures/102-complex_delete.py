#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())
    for v in list_keys:
        if value == a_dictionary.get(v):
            del a_dictionary[v]
    return a_dictionary
