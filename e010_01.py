#!/bin/env python

from pprint import pprint
import sys, time


def IsPrime(num):
    if num == 1:
        return False
    counter = 2
    while counter < num:
        if not num % counter:
            return False
        counter += 1
    return True

def IsSoEPrime(num, prime, composite):
    for p in prime:
        if not num % p:
            composite.add(num)
            return prime, composite
        else:
            prime.add(num)
            return prime, composite


def MultipleGenerator(num, limit):
    return [num*i for i in xrange(limit+1) if num*i < limit+1]



def SoE(limit):
    primes = list()
    done = False
    prime = list([i for i in xrange(3, limit+1, 2)])
    prime.sort()
    c = 0
    while not done:
        print len(prime)
        i = prime.pop(0)
        c += 1
        if c <= limit:
            done = True
        print i
        for x in MultipleGenerator(i, limit):
            if x in prime:
                print 'removing {0}'.format(x)
                prime.remove(x)
        prime.append(i)
    prime.append(2)
    print len(prime)
    prime.sort()
    sum = 0
    for p in prime:
        sum += p
    print sum

def Main(limit):
    allprimes = SoE(limit)


if __name__ == '__main__':
    limit = 2000000
    Main(limit)
