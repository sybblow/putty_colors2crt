color2pos = [12, 14, 0, 8, 0, 7, 0, 0, 1, 9, 2, 10, 3, 11, 4, 0, 5, 13, 6, 0, 0, 15]

ocolors = [ None ] * 16

with open('E:\\colors.txt', 'r') as fp:
    for l in fp:
        num, carray, _ = l.split('\\')
        num = int(num[6:])

        carray = carray.split(',')
        c = ['%02x' % int(e) for e in carray]
        c.append('00')

        pos = color2pos[num]
        ocolors[pos] = c

for ostr in (ocolors[0:8], ocolors[8:16]):
    print ' '.join(reduce(lambda x, y: x+y, ostr))