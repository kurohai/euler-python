def get_input(linecount):
    for i in range(linecount):
        yield int(eval(raw_input()))

def main():
    linecount = int(raw_input())
    n = get_input(linecount)
    for x in range(linecount):
        target = int(n.next())
        print modsum(target)

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
