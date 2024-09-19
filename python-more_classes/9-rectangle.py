#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
         Initialize a new Rectangle.

         Args:
             width (int): The width of the rectangle. Defaults to 0.
             height (int): The height of the rectangle. Defaults to 0.
         """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        The area is computed using the formula:
        Area = width * height

        Returns:
            float: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        The perimeter is computed using the formula:
        Perimeter = 2 * (width + height)

        If either the width or height is 0,
        the perimeter will be returned as 0.

        Returns:
            float: The perimeter of the rectangle,
            or 0 if width or height is 0.
        """
        if self.width is 0 or self.height is 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        Returns a string representation of
        the rectangle using the character '#'.

        If either width or height is 0, returns an empty string.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width is 0 or self.__height is 0:
            return ("")
        custom_symbol = str(self.print_symbol)
        string = [custom_symbol * self.__width for _ in range(self.__height)]
        return "\n".join(string)

    def __repr__(self):
        """Return a string representation of the Rectangle object."""

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Destructor for the Rectangle class."""

        print('Bye rectangle...')

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with the greater area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If either rect_1 or rect_2 is not
            an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the greater area.
            If both areas are equal,
                        rect_1 is returned.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new instance of the class with equal width and height."""
        return (cls(size, size))