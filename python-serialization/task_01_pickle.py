#!/usr/bin/python3
"""Define a class CustomObject."""
import pickle


class CustomObject:
    """Custom Python class."""

    def __init__(self, name, age, is_student):
        """
        Constructor for CustomObject.

        Args:
            name (str): The name of the person being represented.
            age (int): The age of the person being represented.
            is_student (bool): Whether or not the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student
        
        
    def displa(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
        
    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error serializing the object: {e}")
        return None
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return None
        except Exception as e:
            print(f"Error deserializing the object: {e}")
            return None
