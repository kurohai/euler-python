#!/bin/env python


def get_fibbo(seq, last):
    return seq + last

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def get_input(linecount):
    for i in range(linecount):
        yield int(eval(raw_input()))

def main():
    linecount = int(raw_input())
    n = get_input(linecount)
    for x in range(linecount):
        max = int(n.next())
        last, fibo = (1, 2)
        sum = 0
        while fibo <= max:
            if is_even(fibo):
                sum += fibo
            tmp = fibo
            fibo = get_fibbo(last, fibo)
            last = tmp
        print sum

if __name__ == '__main__':
    main()
