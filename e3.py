#!/bin/env python


def IsPrime(num):
    counter = 2
    while counter < num:
        if not num % counter:
            return False
        counter += 1
    return True


def IsMultiple(num, t):
    if not t % num:
        return True
    else:
        return False


def increment(num):
    return num + 1


def Main():
    target = 600851475143
    c = 3
    done = False
    while c < 100000:
        c = increment(c)
        chk =  c
        if IsMultiple(chk, target):
            if IsPrime(chk):
                prime = chk
    print prime


if __name__ == '__main__':
    Main()
