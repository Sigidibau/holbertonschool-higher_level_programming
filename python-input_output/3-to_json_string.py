#!/usr/bin/python3
"""Convert a Python object to a JSON string."""


import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object.

    Args:
        my_obj: The Python object to convert.

    Returns:
        str: The JSON string representation of the object.
    """
    recive = json.dumps(my_obj)
    return recive
