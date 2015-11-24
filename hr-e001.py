#!/bin/env python

def count(n):
    return n * (n + 1) / 2

def get_input(linecount):
    for i in range(linecount):
        yield int(eval(raw_input()))

def main():
    linecount = int(raw_input())
    n = get_input(linecount)
    for x in range(linecount):
        target = int(n.next()) - 1
        print count(target/3) * 3 + count(target/5) * 5 - count(target/15) * 15

if __name__ == '__main__':
    main()
