#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    i = 0
    best = ''
    for x, y in a_dictionary.item():
        if y > i:
            i = y
            best = x
    return best
