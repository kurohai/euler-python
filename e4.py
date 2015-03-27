#!/bin/env python


def IsPalindrome(num):
    snum = str(num)
    max = len(snum) / 2
    c = 0
    if num < 10:
        return True
    while c <= max:
        c += 1
        if not snum[c-1] == snum[-c]:
            return False
    return True


def GetAllMultiples(num):
    """returns all multiples between 800 and 1000 of a number"""
    c = 1000
    multiples = set()
    while c:
        c -= 1
        multiples.add(GetMultiple(c, num))
    return multiples


def GetMultiple(num1, num2):
    """returns the multiple of any number"""
    return num1 * num2

def Main():
    max = GetMultiple(999,999)
    multi = set()
    for i in xrange(800, 1000):
        multi.update(GetAllMultiples(i))
    for i in multi:
        if i > 900000:
            if IsPalindrome(i):
                print i



if __name__ == '__main__':
    Main()
