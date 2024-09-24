#!/usr/bin/python3
"""
Class BaseGeometry
Class Rectangle
Class Square
"""


Rectangle = __import__('9-rectangle.py').Rectangle
"""superclass import """


class Square(Rectangle):
    """Square class that inherits from rectangle class.

    Args:
        Rectangle (class): class to inherit from.
    """

    def __init__(self, size):
        """Instantiation with size.

        Args:
            size (int): The size of the square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
