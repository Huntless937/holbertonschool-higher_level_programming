#!/usr/bin/python3
"""Module that contains the inherits_from function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if obj inherited (directly or indirectly) from a_class,
              but is not an instance of a_class itself. Otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
