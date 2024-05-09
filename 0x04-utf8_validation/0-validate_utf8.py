#!/usr/bin/python3
"""
Define UTF-8 Validation function
"""


def validUTF8(data):
    """
    UTF-8 Validation
    """
    tes = 1 << 7
    spa = 1 << 6
    byteCount = 0
    for codePoint in data:
        elon = 1 << 7
        if byteCount == 0:
            while elon & codePoint:
                byteCount += 1
                elon = elon >> 1
            if byteCount == 0:
                continue
            if byteCount == 1 or byteCount > 4:
                return False
        else:
            if not (codePoint & tes and not (codePoint & spa)):
                return False
        byteCount -= 1
    return not byteCount
