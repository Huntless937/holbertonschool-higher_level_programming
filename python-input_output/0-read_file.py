#!/usr/bin/python3
"""
Module that contains a function that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a UTF8 text file and prints its content to stdout.
    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
