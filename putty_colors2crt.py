from __future__ import print_function
from itertools import tee, islice, izip


color2pos = [8, 0, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]
line_size = 8

ocolors = [ None ] * 16

with open('E:\\colors.txt', 'r') as fp:
    r = [
        (lambda num, array:(
            int(num[6:]),
            ['%02x' % int(e) for e in array.split(',')] + ['00']))
        (
            *((lambda t:(
                t[0],
                t[1]))
            (l.split('\\'))))
        for l in fp
    ]

    r = [ (color2pos[num-6], c) for num, c in r if num >= 6 ]

    for pos, c in r:
        ocolors[pos] = c

    map(
        print,
        map(
            lambda l:
                ' '.join(
                    reduce(
                        lambda x, y: x+y,
                        l)),
            # split into line_size pieces
            # there is also a grouper recipe: https://docs.python.org/2/library/itertools.html#recipes
            izip(
                *[islice(l, i, None, line_size) for i, l in
                    enumerate(
                        tee(ocolors, line_size))])))