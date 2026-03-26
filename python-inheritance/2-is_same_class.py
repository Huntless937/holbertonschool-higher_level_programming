#!/usr/bin/python3
"""Module that contains the is_same_class function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) is a_class
