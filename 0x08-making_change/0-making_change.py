#!/usr/bin/python3
""" Changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total
    """
    if total <= 0:
        return 0
    check = 0
    tem = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            tem += 1
        if check == total:
            return tem
        check -= i
        tem -= 1
    return -1
