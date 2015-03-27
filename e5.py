#!/bin/env python


def IsDivisible(num1, num2):
    if num1 % num2:
        return False
    else:
        return True

def CheckAll(num):
    if not IsDivisible(num, 2):
        return False
    if not IsDivisible(num, 3):
        return False
    if not IsDivisible(num, 4):
        return False
    if not IsDivisible(num, 5):
        return False
    if not IsDivisible(num, 6):
        return False
    if not IsDivisible(num, 7):
        return False
    if not IsDivisible(num, 8):
        return False
    if not IsDivisible(num, 9):
        return False
    if not IsDivisible(num, 10):
        return False
    if not IsDivisible(num, 11):
        return False
    if not IsDivisible(num, 12):
        return False
    if not IsDivisible(num, 13):
        return False
    if not IsDivisible(num, 14):
        return False
    if not IsDivisible(num, 15):
        return False
    if not IsDivisible(num, 16):
        return False
    if not IsDivisible(num, 17):
        return False
    if not IsDivisible(num, 18):
        return False
    if not IsDivisible(num, 19):
        return False
    if not IsDivisible(num, 20):
        return False
    return True


def Main():
    chkme = [i for i in xrange(10000000, 1000000001, 20) if not i % 20]
    print 'numbers to check: {0}'.format(len(chkme))
    for c in chkme:
        if CheckAll(c):
            return c
    return 'None Found'


if __name__ == '__main__':
    print Main()
