#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special = ".?:"
    i = 0
    clean_text = text.strip()
    while i < len(clean_text):
        print(clean_text[i], end="")
        if clean_text[i] in special:
            print("\n")
            i += 1
            while i < len(clean_text) and clean_text[i] == ' ':
                i += 1
            continue
        i += 1
