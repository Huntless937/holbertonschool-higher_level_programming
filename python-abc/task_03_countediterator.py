#!/usr/bin/env python3
"""
Module for CountedIterator class.
This module demonstrates how to extend an iterator to keep track of counts.
"""


class CountedIterator:
    """
    An iterator that keeps track of the number of items iterated.
    """

    def __init__(self, some_iterable):
        """
        Initializes the CountedIterator with an iterable.
        Args:
            some_iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(some_iterable)
        self.__counter = 0

    def get_count(self):
        """
        Returns the current number of items that have been iterated.
        """
        return self.__counter

    def __next__(self):
        """
        Fetches the next item and increments the counter.
        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.__counter += 1
            return item
        except StopIteration:
            raise StopIteration
