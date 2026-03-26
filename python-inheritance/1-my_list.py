#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """A class MyList that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
