#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Public instance method that calculates area.

        Raises:
            Exception: with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")
