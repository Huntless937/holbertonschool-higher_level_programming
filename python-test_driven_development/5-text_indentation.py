#!/usr/bin/python3
"""
This module provides a function for text indentation.
It adds two new lines after specific characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    There should be no space at the beginning or end of each printed line.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Xüsusi simvolların siyahısı
    chars = [".", "?", ":"]

    # Cari sətirin başındakı boşluğu idarə etmək üçün flag
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in chars:
            print("\n")
            i += 1
            # Növbəti sətirin başındakı bütün boşluqları atla
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
