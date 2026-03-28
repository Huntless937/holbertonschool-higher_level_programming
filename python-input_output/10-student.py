#!/usr/bin/python3
"""
Defines a Student class with attribute filtering.
"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student.
        If attrs is a list of strings, filter attributes.
        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
