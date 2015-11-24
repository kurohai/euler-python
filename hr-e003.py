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

def get_input(linecount):
    for i in range(linecount):
        yield int(eval(raw_input()))

def main(linecount):
    n = get_input(linecount)
    for line in range(linecount):
        target = int(n.next())
        c = 3
        done = False
        while c <= target:
            c += 1
            chk =  c
            if IsMultiple(chk, target):
                if IsPrime(chk):
                    prime = chk
        print prime

if __name__ == '__main__':
    main(int(raw_input()))
