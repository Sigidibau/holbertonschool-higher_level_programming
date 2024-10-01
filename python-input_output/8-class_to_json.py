#!/usr/bin/python3
"""Clas to json"""


import json


def class_to_json(obj):
    """
    Convert a class instance to a dictionary representation.

    This function takes an object as input and returns a dictionary
    containing the instance variables of the object. The dictionary
    can be easily serialized to JSON format.

    Parameters:
    obj: Any instance of a class

    Returns:
    dict: A dictionary representation of the object's instance variables.
    """
    return obj.__dict__
