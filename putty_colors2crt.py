import sys

color2pos = [8, 0, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]

ocolors = [None] * 16

for l in sys.stdin:
    num, carray, _ = l.split('\\')
    num = int(num[6:])

    carray = carray.split(',')
    c = ['%02x' % int(e) for e in carray]
    c.append('00')

    if num >= 6:
        pos = color2pos[num - 6]
        ocolors[pos] = c

for ostr in (ocolors[0:8], ocolors[8:16]):
    print ' '.join(reduce(lambda x, y: x + y, ostr))
