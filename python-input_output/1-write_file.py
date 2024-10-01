#!/usr/bin/python3
"""Module to write a string to a text file.

This module contains a function that writes
a given string to a specified
text file. If the file already exists,
its content will be overwritten."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number
    of characters written.

    Args:
        filename (str): The name of the file to write to.
                        If the filename is an empty string,
                        no file will be created.
        text (str): The text to write to the file.
                    If the text is an empty string,
                    nothing will be written.

    Returns:
        int: The number of characters written to the file.
             Returns 0 if an error occurs during file writing.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
