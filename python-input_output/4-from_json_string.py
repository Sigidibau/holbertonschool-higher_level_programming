#!/usr/bin/python3
"""Convert a JSON string to a Python object."""


import json


def from_json_string(my_str):
    """Convert a JSON-formatted string to a Python object.

    Args:
        my_str (str): A string containing JSON data.

    Returns:
        The corresponding Python object.
    """
    recive = json.loads(my_str)
    return recive
