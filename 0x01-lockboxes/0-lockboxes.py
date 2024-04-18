#!/usr/bin/python3
"""
lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether eries of locked boxes can be opened
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_ = False
        for idx in range(len(boxes)):
            boxes_ = k in boxes[idx] and k != idx
            if boxes_:
                break
        if boxes_ is False:
            return boxes_
    return True
