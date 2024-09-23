#!/usr/bin/python3\
"""Defining a function"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a class that
    is a subclass (direct or indirect) of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if `obj` is an instance of a subclass of `a_class`
              (but not an instance of `a_class` itself),
              False otherwise.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
