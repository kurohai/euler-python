#!/bin/env python


def Main(limit):
    lattice = dict()
    currow = 0
    lattice[currow] = list()
    for i in xrange(0, limit):
        lattice[currow].append(1)
    currow += 1
    lattice[currow] = list()
    for i in xrange(0, limit):
        lattice[currow].append(1+i)
    for i in xrange(0, limit):
        currow += 1
        lattice[currow] = list()
        for i in xrange(0, limit):
            if i == 0:
                point = 1
            else:
                last_point = lattice[currow][i-1]
                last_lat = lattice[currow-1][i]
                point = last_point + last_lat
                if point == 137846528820:
                    return point
            lattice[currow].append(point)


if __name__ == '__main__':
    limit = 21
    print 'answer: {0}'.format(Main(limit))
