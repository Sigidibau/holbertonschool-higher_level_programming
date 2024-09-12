#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, int, float)):
        rise TypeError('a mustbe an integer')
    if not isinstance(b, int, float)):
        rise TypeError('b, must be an integer')
        return int(a) + int(b)
