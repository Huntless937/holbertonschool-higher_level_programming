#!/usr/bin/python3
"""Module that defines a BaseGeometry class with validation."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Public instance method that calculates area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
