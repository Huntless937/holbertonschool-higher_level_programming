#!/usr/bin/python3
"""Module that defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        # Hər yeni sətir həmişə 1 ilə başlayır
        new_row = [1]
        
        # Aradakı rəqəmləri hesabla (üst sətirdəki qonşuların cəmi)
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
            
        # Sətri 1 ilə bitir
        new_row.append(1)
        triangle.append(new_row)

    return triangle
