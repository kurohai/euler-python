#!/bin/env python


def TriangleGenerator(num):
    sum = 0
    while num >= 0:
        sum += num
        num -= 1
    return sum


def divisorGenerator(n):
    large_divisors = list()
    for i in xrange(1, int((n**0.5) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor


def Main():
    for i in xrange(1, 999999, 2):
        print 'i:\t{0}'.format(i)
        tan = TriangleGenerator(i)
        print 'tan:\t{0}'.format(tan)
        fac = list(divisorGenerator(tan))
        print 'fac:\t{0}'.format(len(fac))
        if len(fac) >= 500:
            print 'i: {0}'.format(i)
            print 'tan: {0}'.format(tan)
            print(len(fac))
            return tan


if __name__ == '__main__':
    answer = Main()
    print 'answer: {0}'.format(answer)
