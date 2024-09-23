#!/usr/bin/python3
"""Define a functio"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class or
    a subclass thereof.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class` or
              an instance of a subclass of `a_class`;
              False otherwise.
    """
    return isinstance(obj, a_class)
