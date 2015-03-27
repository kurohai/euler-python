#!/bin/env python

def square(num):
    return num * num

def sqrt(num):
    return num ** (0.5)


def Main():
    allsquares = [square(s) for s in xrange(1, 1001)]
    for a in allsquares:
        for b in allsquares:
            c = a + b
            if c in allsquares:
                art = sqrt(a)
                brt = sqrt(b)
                crt = sqrt(c)
                if art + brt + crt == 1000:
                    print int(art * brt * crt)
                    return


if __name__ == '__main__':
    Main()
