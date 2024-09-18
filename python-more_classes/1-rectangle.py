#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """
         Initialize a new Rectangle.

         Args:
             width (int): The width of the rectangle. Defaults to 0.
             height (int): The height of the rectangle. Defaults to 0.
         """
        self.width = width
        self.height = height


@property
def width(self):
    """
Get the width of the rectangle.

Returns:
    int: The width of the rectangle.
    """
    return self.__width


@width.setter
def width(self, value):
    """
    Set the width of the rectangle.

    Args:
        value (int): The new width of the rectangle.

    Raises:
        TypeError: If `value` is not an integer.
        ValueError: If `value` is less than 0.
    """
    if not isinstance(width, int):
        raise TypeError('width must be an integer')
    if width < 0:
        raise ValueError('Width must be >= 0')
    self.__width = value


@property
def height(self):
    """
    Get the height of the rectangle.

    Returns:
        int: The height of the rectangle.
    """
    return self.__height


@height.setter
def height(self, value):
    """
    Set the height of the rectangle.

    Args:
        value (int): The new height of the rectangle.

    Raises:
        TypeError: If `value` is not an integer.
        ValueError: If `value` is less than 0.
    """
    if not isinstance(value, int):
        if not height(height, int):
            raise TypeError('heigth must be and integer')
    if height < 0:
        raise ValueError('height must be >= 0')
    self.__height = value
