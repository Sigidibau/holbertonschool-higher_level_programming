#!/usr/bin/python3
"""Module to define a Student class with JSON serialization."""


class Student:
    """Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(self):
    """Converts the Student instance to a JSON-compatible dictionary.

        Returns:
            dict: A dictionary representation of
            the Student instance's attributes.
    """
    return self.__dict__
