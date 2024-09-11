#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0 for i in range(list_length)]
    for i in range(list_lenght):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print('Wrong typr')
        except IndexError:
            print('Out of range')
        finally:
            pass
        return new_list
