#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for c in my_string:
        if c in "cC":
            pass
        else:
            new_string.append(c)

    return "".join(new_string)
