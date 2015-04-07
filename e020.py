#!/bin/env python

def Multiply(num1, num2):
    """returns the product of any two numbers"""
    return num1 * num2

def Factorial(num):
    if num == 1:
        return num
    i = num
    while i > 1:
        i -= 1
        num = Multiply(num, i)
    return num

def AddDigits(num):
    num = str(num)
    a = 0
    for i in num:
        a += int(i)
    return a

def Main(limit):
    fac = Factorial(limit)
    return AddDigits(fac)


if __name__ == '__main__':
    limit = 100
    print Main(limit)
