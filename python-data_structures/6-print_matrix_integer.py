#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in i:
            print("{:d}".format(x), end="" if x == i[-i] else " ")
        print()
