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

    def integer_validator(self, name, value):
        """
        Validate that the given value is a positive integer.

        Parameters:
            name (str): The name of the variable being validated,
            used for error messages.
            value (any): The value to be validated.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.

        Returns:
            int: The validated integer value.
        """
        if not isinstance(value, int):
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
        return value
