#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d = a_dictionary.copy()
    for k, v in d.items():
        if value in v:
            del d[k]
    return a_dictionary
