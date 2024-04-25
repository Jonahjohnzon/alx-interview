#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    there is a single character H.
    """

    if n <= 1:
        return 0
    numb, div, numOfOperations = n, 2, 0

    while numb > 1:
        if numb % div == 0:
            numb = numb / div
            numOfOperations = numOfOperations + div
        else:
            div += 1
    return numOfOperations
