#!/usr/bin/python3
"""Define a class named Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int, optional): Private instance attribute. Defaults to 0.

        Raises:
            TypeError: if size isn't an integer.
            ValueError: if size < 0
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: if value isn't an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """function to get the area of a square

        Returns:
            int: the size of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using '#' characters."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print('#' * self.__size)
