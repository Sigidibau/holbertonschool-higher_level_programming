#!/usr/bin/python3
"""Save an object to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to save the JSON data.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        recive = json.dumps(my_obj)
        f.write(recive)
