#!/usr/bin/env python3
"""
This module defines the VerboseList class that inherits from the 
built-in list class and provides notifications for modifications.
"""


class VerboseList(list):
    """
    A custom list class that prints a message whenever an item 
    is added or removed using specific methods.
    """

    def append(self, item):
        """Adds an item to the list and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list with items and prints a notification."""
        num_items = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(num_items))

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list and prints a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
