#!/usr/bin/python3
"""Define a class named Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=0(0, 0)):
        """Initialize a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional):\
                The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: if size isn't an integer or if position isn't\
                a tuple of 2 integers.
            ValueError: if size < 0 or if any coordinate\
                in position is negative.
        """
        self.__size = size
        self.__position = position

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

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: if value isn't a tuple of 2 integers.
            ValueError: if any coordinate in the tuple is negative.
        """
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError('size must be an integer')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('size must be and integer')
        elif type(value[0]) < 0 or type(value[1]) < 0:
            raise TypeError('size must be and integer')
        self.__position = value

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
