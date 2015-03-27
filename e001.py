#!/bin/env python


def mfive(num):
    p = num * 5
    if p < 1000:
        return p
    else:
        return 0


def mthree(num):
    p = num * 3
    if p < 1000:
        return p
    else:
        return 0


def Main():
    sum = 0
    done = set()
    for i in xrange(1000):
        m = mfive(i)
        done.add(m)
        m = mthree(i)
        done.add(m)

    for d in done:
        sum += d
    print sum


if __name__ == '__main__':
    Main()
