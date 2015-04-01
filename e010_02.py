#!/bin/env python


def SoE(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False
                print 'removing: {0}'.format(n)


def Main(limit):
    sum = 0
    for i in SoE(limit):
        sum += i
    return sum


if __name__ == '__main__':
    limit = 2000000
    answer = Main(limit)
    print answer
