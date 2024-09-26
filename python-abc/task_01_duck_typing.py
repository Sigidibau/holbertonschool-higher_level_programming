#!/usr/bin/python3
"""A module for calculating area and perimeter of shapes."""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""

        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""

        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""

        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""

        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""

        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""

        return 2 * (self.width + self.height)


def shape_info(Shape):
    """Print the area and perimeter of a given shape.

    Args:
        shape (Shape): An instance of a Shape subclass.

    This function calls the `area` and `perimeter` methods
    of the given shape and prints their values to the console.
    """
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
