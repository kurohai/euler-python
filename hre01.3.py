import time
def multiple(num, multi, target):
    p = num * multi
    if p < target:
        return p
    else:
        return 0

def get_input(linecount):
    for i in range(linecount):
        yield int(eval(raw_input()))

def main():
    linecount = int(raw_input())
    n = get_input(linecount)
    for x in range(linecount):
        target = int(n.next())
        start = time.time()
        sum = modsum(target)
        end = time.time()
        print end - start, sum
        start = time.time()
        sum = setsum(target)
        end = time.time()
        print end - start, sum

def setsum(target):
    sum = 0
    done = set()
    for i in range(target):
        done.add(multiple(i, 3, target))
        done.add(multiple(i, 5, target))
    for d in done:
        sum += d
    return sum

def listsum(target):
    sum = 0
    done = list()
    for i in range(target):
        done.append(multiple(i, 3, target))
        done.append(multiple(i, 5, target))
    done = set(done)
    for d in done:
        sum += d
    return sum

def modsum(target):
    sum = 0
    done = set()
    for i in range(target):
        if not i % 3:
            done.add(i)
        elif not i % 5:
            done.add(i)
    for d in done:
        sum += d
    return sum



if __name__ == '__main__':
    main()
