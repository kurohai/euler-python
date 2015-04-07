#!/bin/env python

import time

starttime = time.time()

def CollatzSequence(num):
    all_vals = list()
    all_vals.append(num)
    while num != 1:
        if even(num):
            num = (num / 2)
        else:
            num = (3 * num) + 1
        all_vals.append(num)
    return len(all_vals)


def even(num):
    if not num % 2:
        return True
    else:
        return False


def Main():
    largest = 0
    for i in xrange(1, 1000001):
        seq = CollatzSequence(i)
        if seq > largest:
            largest = seq
            print i
    print largest


if __name__ == '__main__':
    Main()
    endtime = time.time()
    print endtime - starttime
