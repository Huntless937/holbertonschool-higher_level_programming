#!/usr/bin/env python3
"""
This module defines the Shape abstract class and its subclasses,
Circle and Rectangle, along with a duck typing function shape_info.
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
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initializes Circle with radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

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
    Prints area and perimeter using duck typing.
    Trusts that the object has area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
