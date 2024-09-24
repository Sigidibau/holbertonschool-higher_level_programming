#!/usr/bin/python3
"""
Class BaseGeometry
Class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
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
