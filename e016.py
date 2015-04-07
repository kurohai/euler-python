#!/bin/env python


def power(base, expo):
    return base ** expo

def Main(base, expo):
    bignumber = str(power(base, expo))
    answer = 0
    for n in bignumber:
        answer += int(n)

    return answer



if __name__ == '__main__':
    print Main(2, 1000)
