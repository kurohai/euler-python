#!/bin/env python

import sys

def Main(next, itr, sequence):
    seq = seqgen(next, sequence)
    a = 0
    for s in seq:
        a += int(s)
    if a != 15:
        print 'ERROR IN SEQUENCE'
        sys.exit(0)
    mod = itr % 15
    prefix = (itr / 15) * seq
    if not mod:
        return prefix
    else:
        i = 0
        done = False
        value = prefix
        next = GetSequence(i)
        print 'init next: {0}'.format(next)
        print 'init seq : {0}'.format(seq[next])

        while not done:
            # counter stuff
            i += 1

            # get next sequence
            suffix = str(seq[next])

            # add next sequence
            value = '{0}{1}'.format(value, suffix)
            print value

            # check for done
            val = 0
            for v in value:
                val += int(v)
            if val == itr:
                done = True
                return value, next
            else:
                next = GetSequence(i+1)

            # prevent loops
            if i > 14:
                sys.exit(1)


def Shortcut(next, itr):
    next = 0
    itr = 189
    mod = itr % 15
    div = itr / 15
    if not mod:
        pass
    else:
        print 'next: {0}'.format(next)
        print 'mod:  {0}'.format(mod)
    return next

def GetSequence(num):
    while num > 6-1:
        num -= 6
    return num

def GetNext(num):
    return GetSequence(num+1)


def seqgen(next, seq):
    lol = [seq[GetNext(s)] for s in xrange(next, next+5)]
    rofl = str(seq[next])
    for l in lol:
        rofl += str(l)
    return rofl


if __name__ == '__main__':
    seq = '123432'
    print Main()
