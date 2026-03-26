#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The function is designed to handle both integers and floats.
Floats are casted to integers before the operation.
This ensures the return value is always an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    a and b must be integers or floats.
    Returns the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Float overflow (inf) və NaN yoxlaması
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
