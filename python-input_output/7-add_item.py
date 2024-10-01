#!/usr/bin/python3
"""This module provides functionality to manage a list of items
stored in a JSON file. It allows users to append new items
provided as command-line arguments to an existing list in the
file, or create a new list if the file does not exist.

The operations include:
- Loading the existing list from a JSON file.
- Appending new items to the list.
- Saving the updated list back to the JSON file.
"""


import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
