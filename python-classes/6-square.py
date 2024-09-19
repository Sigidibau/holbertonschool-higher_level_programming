#!/usr/bin/python3
"""Define a class named Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int, optional): The size of the square.
            Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: if size isn't an integer or
            if position isn't a tuple of 2 integers.
            ValueError: if size < 0 or
            if any coordinate in position is negative.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return (self.__size)

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
    def position(self):
        """Get the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: if value isn't a tuple of 2 integers.
            ValueError: if any coordinate in the tuple is negative.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 integers')
        if not all(isinstance(coord, int) for coord in value):
            raise TypeError('position must be a tuple of 2 integers')
        if any(coord < 0 for coord in value):
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size) ** 2

    def my_print(self):
        """Prints the square using '#' characters with correct position."""
        if self.__size == 0:
            print("")
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print the square
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
