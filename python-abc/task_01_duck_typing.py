#!/usr/bin/env python3
"""
This module defines an abstract class Shape and its subclasses
Circle and Rectangle. It also includes a function shape_info
that demonstrates the concept of duck typing in Python.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract Base Class for geometric shapes.
    Ensures that all subclasses implement area and perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents a circle shape.
    Inherits from Shape.
    """

    def __init__(self, radius):
        """
        Initializes a Circle with a specific radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle shape.
    Inherits from Shape.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of any object that
    implements area() and perimeter() methods.
    Demonstrates duck typing (no isinstance check).
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
