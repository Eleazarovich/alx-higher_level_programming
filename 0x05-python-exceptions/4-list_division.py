#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    invalid = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            invalid = 1
        except ZeroDivisionError:
            print("division by 0")
            invalid = 1
        except IndexError:
            print("out of range")
            invalid = 1
        finally:
            if invalid:
                invalid = 0
                new_list.append(invalid)
            else:
                new_list.append(result)
    return new_list
