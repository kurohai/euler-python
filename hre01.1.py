def get_last(target, d):
    mod = target % d
    while mod:
        target -= 1
        mod = target % d
    return target

def get(target, d):
    f = d
    l = get_last(target, d)
    n = (l / f)
    return (n / 2) * ((2 * f) + ((n - 1) * d))


target = 100000000
print get(target, 3) + get(target, 5)

