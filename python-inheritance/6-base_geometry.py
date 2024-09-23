#!/usr/bin/python3
"""BaseGeometry class that defines an interface for geometric shapes."""


class BaseGeometry:
    def area(self):
        """Calculate the area of the shape.

        This method should be overridden in subclasses. If called
        directly, it raises an Exception indicating that the method
        is not implemented.
        """
    raise Exception("area() is not implemented")
