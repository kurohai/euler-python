#!/bin/env python

import os

def GetResource():
    res = os.path.abspath('./res/otdn.txt')
    with open(res, 'rb') as f:
        content = f.readlines()
    return content[0].strip()


def GetLargest(listofints):
    s = 0
    for i in listofints:
        if i > s:
            s = i
    return s


def GetProduct(sequence):
    i = 1
    prod = sequence[0]
    while i < 13:
        prod = int(prod) * int(sequence[i])
        i += 1
    return int(prod)


def Main():
    odtn = GetResource()
    fn = 0
    ln = 13
    lop = list()
    while ln < 1001:
        sequence = odtn[fn:ln]
        if '0' not in sequence:
            lop.append(GetProduct(sequence))
        fn += 1
        ln += 1
    answer = GetLargest(lop)
    print answer


if __name__ == '__main__':
    Main()
