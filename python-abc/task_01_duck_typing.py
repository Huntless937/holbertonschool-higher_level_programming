#!/usr/bin/env python3
"""
Module for Shape, Circle, Rectangle and shape_info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class that defines a Circle."""

    def __init__(self, radius):
        """Initializes Circle with radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class that defines a Rectangle."""

    def __init__(self, width, height):
        """Initializes Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape object
    using duck typing.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
