#!/usr/bin/python3
"""BaseGeometry class for geometric shapes.

This abstract class defines a blueprint for geometric shapes. It requires
subclasses to implement the `area` method, which should calculate the area
of the specific shape. The class cannot be instantiated directly.

Attributes:
    None

Methods:
    area() -- Raises an Exception indicating that the method is
    not implemented.
"""


class BaseGeometry:
    """Geometry class"""
    def area(self):
        """Calculate the area of the shape.

        This method is meant to be overridden in subclasses to provide
        specific implementations for calculating the area. If called
        on an instance of BaseGeometry, it raises an Exception indicating
        that the method is not implemented.

        Raises:
            Exception: If called directly without being overridden.
        """
        raise Exception("area() is not implemented")
