#!/usr/bin/python3


def read_file(filename=""):
    """
    Reads the content of a text file and returns it as a string.

    Args:
        filename (str): The path to the file to be read.
                        Defaults to an empty string, which should be replaced
                        with a valid file path when calling the function.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
