#!/usr/bin/python3
"""Load data from a JSON file"""


import json


def load_from_json_file(filename):
    """Reads a JSON file and returns the corresponding Python object."""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f)
