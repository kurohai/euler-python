#!/bin/env python


def IsPrime(num):
    if num == 1:
        return False
    counter = 2
    while counter < num:
        if not num % counter:
            return False
        counter += 1
    return True



def Main(count):
    done = False
    i = 1
    primes = list()
    while not done:
        i += 2
        if IsPrime(i):
            primes.append(i)
            print '{0}\t{1}'.format(len(primes), i)
        if len(primes) == count:
            done = True
    print primes[-1]


if __name__ == '__main__':
    Main(10001)
