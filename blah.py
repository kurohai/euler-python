
def get_input(linecount):
    for i in range(linecount):
        yield eval(raw_input())

def parse_cmd(s):
    s = s.lower()
    if 'append' in s:
        return list.append


def parse_line(line):
    vals = line.split(' ')
    cmd = parse_cmd(vals[0])
    print cmd


    return dict(c=cmd, val=1)

def do_cmd(L, cb):
    pass


def main():
    linecount = int(raw_input())
    L = list()
    n = get_input(linecount)
    for x in range(linecount):
        line = parse_line(n.next())

        print line['c'](['a'], line['val'])



if __name__ == '__main__':
    main()





    def parse_line(row, col):
        if not row % 2:
            start = 1
            i = row / 2
        else:
            start = 0
            i = (row / 2) + 1
        while i > 1000:
            start += 100
            i -= 10
        return start, i

    def parse_line2(row, col):
        i = (row / 2) + (row % 2)
        start = 0
        if not row % 2:
            start += 1
        while i > 100:
            start += 100
            i -= 10
        return start, i


    def main():
        row, col = raw_input().split(' ')

        # start, i = parse_line2(int(row), int(col))
        start, i = parse_line(int(row), int(col))
        for r in range(i-1):
            start = start + 10
        for c in range(int(col)-1):
            start += 2
        print start



    if __name__ == '__main__':
        main()


        with open('/mnt/db/hrlist', 'w+') as f:

            o = -1
            e = -2
            for r in range(10**8):
                orow = list()
                erow = list()
                for c in range(5):
                    o += 2
                    e += 2
                    orow.append(o)
                    erow.append(e)
                f.write(str(erow) + '\n')
                f.write(str(orow) + '\n')




                o = -1
                e = -2
                for r in range(10**):
                    orow = list()
                    erow = list()
                    for c in range(5):
                        o += 2
                        e += 2
                        orow.append(o)
                        erow.append(e)
                    print(str(erow) + '\n')
                    print(str(orow) + '\n')





                    def get_input(linecount):
                        for i in range(linecount):
                            yield long(eval(raw_input()))

                    def do_loop(c):
                        n = 0
                        for i in range(2, 1+c):
                            last = i - 1
                            n = last + n
                        print n

                    def main():
                        linecount = int(raw_input())
                        count = get_input(linecount)
                        for line in xrange(linecount):

                            do_loop(count.next())


                    if __name__ == '__main__':
                        main()



                        def do_loop(pattern):
                            match = list()
                            if ' ' in pattern:
                                pattern = pattern.split(' ')
                            elif '-' in pattern:
                                match.extend(pattern.split('-'))
                            else:
                                match.append(pattern)
                            return match

                        def get_input(linecount):
                            for i in range(linecount):
                                yield (raw_input())

                        def main():
                            linecount = int(raw_input())
                            count = get_input(linecount)
                            for line in xrange(linecount):

                                c, a, n = do_loop(count.next())
                                print  'CountryCode={c},LocalAreaCode={a},Number={n}'.format(
                                    a=a,
                                    c=c,
                                    n=n,
                                )

                        if __name__ == '__main__':
                            main()

                            148-809-2561957985
