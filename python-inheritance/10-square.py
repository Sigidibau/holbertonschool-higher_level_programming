#!/usr/bin/python3
"""
Class BaseGeometry
Class Rectangle
Class Square
"""


BaseGeometry = __import__('9-rectangle.py').BaseGeometry
"""superclass import """


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int or float: The area of the rectangle,
            calculated as width multiplied by height.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string in the format '[Rectangle] width/height',
            where width and height are the dimensions of the rectangle.
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """Represents a square, inheriting from the Rectangle class."""

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The length of the sides of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
