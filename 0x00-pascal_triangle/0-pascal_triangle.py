#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    """
    ka = []
    if n <= 0:
        return ka
    ka = [[1]]
    for i in range(1, n):
        tep = [1]
        for j in range(len(ka[i - 1]) - 1):
            curr = ka[i - 1]
            tep.append(ka[i - 1][j] + ka[i - 1][j + 1])
        tep.append(1)
        ka.append(tep)
    return ka
