#!/bin/env python

def GetFibbo(seq, last):
    return seq + last

def IsEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def docalc(last, fibo, max):
    sum = 0
    while fibo < max:
        if IsEven(fibo):
            sum += fibo
        tmp = fibo
        fibo = GetFibbo(last, fibo)
        last = tmp

    return sum

print docalc(1, 2, 4000000)
