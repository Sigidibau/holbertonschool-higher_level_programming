#!/usr/bin/python3
"""A module for calculating area and perimeter of shapes."""


from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

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
        pass

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        pass


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, heigth):
        """Initialize the rectangle with width and height."""

        self.width = width
        self.heigth = heigth

    def area(self):
        """Calculate the area of the rectangle."""

        pass

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        pass


def shape_info():
    """Print the area and perimeter of a given shape.

    Args:
        shape (Shape): An instance of a Shape subclass.
    """

    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
