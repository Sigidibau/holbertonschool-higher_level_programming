#!/usr/bin/python3
"""BaseGeometry class that defines an interface for geometric shapes.

The BaseGeometry class is an abstract class that provides a blueprint
for geometric shapes. It includes an abstract method `area`, which must
be implemented by any subclass. This class is intended to be
inherited by other classes that represent specific geometric figures.
"""


class BaseGeometry:
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
