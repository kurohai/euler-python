#!/bin/env python

import sys
import e506other

def DoOld(next, answer, itr):
    print 'startng on:', itr
    print 'this seq beg: {0}'.format(seq[next])
    loops = 0
    done = False
    this = str()
    if itr > 15:
        print 'begining shortcut:', itr
        this, next = e506other.Main(next, itr, seq)
        that = 0
        for a in this:
            that += int(a)
        print 'testing this: {0}'.format(this)
        print 'testing that: {0}'.format(that)
        if that == itr:
            done = True
            answer += int(this)
            print 'done = True'
            print 'from shortcut'
            next = GetSequence(next+1)
            print 'NEXT seq begins: {0}'.format(seq[next])
            print 'clock for {itr} is {ans}\n\n\n'.format(itr=itr, ans=this)
            return next, answer
        else:
            print 'bad shortcut'

    while not done:
        loops += 1
        print 'first this:', this
        this += seq[next]
        print 'second this:', this
        that = 0
        for a in this:
            that += int(a)
        print 'this current: {0}'.format(that)
        next = GetNext(next)

        if this:
            that = 0
            for a in this:
                that += int(a)
            if that == itr:
                done = True
                answer += int(this)
                print 'done = True'
                print 'next seq begins: {0}'.format(seq[next])
                print 'clock for {itr} is {ans}\n\n\n'.format(itr=itr, ans=this)
                return next, answer

        # prevent infinite loops
        if loops > 100:
            raise
    print 'clock for {itr} is {ans}\n\n\n'.format(itr=itr, ans=this)
    return next, answer

def Main(num, *args, **kwargs):
    meth = kwargs.get('meth', None)
    if meth == 99:
        print 'lol meth'
    else:
        next = 0
        answer = 0
        for i in xrange(1, num+1):
            next, answer = DoOld(next, answer, i)
        return answer


def GetSequence(num):
    while num > 5:
        num -= 6
    return num


def GetNext(num):
    return GetSequence(num+1)


if __name__ == '__main__':
    seq = '123432'
    answer = Main(10**3, meth=0)
    print 'answer: {0}'.format(answer%123454321)
