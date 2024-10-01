#!/usr/bin/python3
"""Append text to a file and return the
number of characters added."""


def append_write(filename="", text=""):
    """Append text to a file.

    Args:
        filename (str): The name of the file.
        text (str): The text to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        append_data = f.write(text)
        return append_data
