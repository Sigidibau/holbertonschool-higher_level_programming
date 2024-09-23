#!/usr/bin/python3\
"""_summary_
    """


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
