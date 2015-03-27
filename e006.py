#!/bin/env python


def square(num):
    return num * num


def sum(num1, num2):
    return num1 + num2


def Main():
    squares = 0
    sums = 0
    for i in xrange(101):
        squares += square(i)
        sums += i
    sumsq = square(sums)
    print sumsq - squares



if __name__ == '__main__':
    Main()
