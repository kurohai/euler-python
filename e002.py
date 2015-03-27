#!/bin/env python


def GetFibbo(seq, last):
    return seq + last


def IsEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


def Main(last, fibo, max):
    sum = 0
    while fibo < max:
        if IsEven(fibo):
            sum += fibo
        tmp = fibo
        fibo = GetFibbo(last, fibo)
        last = tmp
    print sum


if __name__ == '__main__':
    Main(1, 2, 4000000)
