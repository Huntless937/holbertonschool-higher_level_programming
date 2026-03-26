#!/usr/bin/python3
"""Module that contains the lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of strings representing attributes and methods.
    """
    return dir(obj)
