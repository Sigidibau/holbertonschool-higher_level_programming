#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length  # Initialize result list with zeros
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i]
            elem_2 = my_list_2[i]
            try:
                if isinstance(elem_1, (int, float)) and
                isinstance(elem_2, (int, float)):
                    result[i] = elem_1 / elem_2
                else:
                    print("wrong type")
            except ZeroDivisionError:
                print("division by 0")
                result[i] = 0
            except IndexError:
                print("out of range")
                break
    return result
