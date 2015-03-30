from __future__ import print_function
from itertools import tee, islice, izip, imap


r = imap(
    lambda l:
    (lambda t: (
        int(t[0][6:]),
        ['%02x' % int(e) for e in t[1].split(',')] + ['00']))
    (l.split('\\')),
    open('colors.txt', 'r')
)

color2pos = [8, 0, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]
r = [(color2pos[num - 6], c) for num, c in r if num >= 6]

output_colors = [None] * 16
for pos, c in r:
    output_colors[pos] = c

line_size = 8
map(
    print,
    imap(
        lambda l:
        ' '.join(
            reduce(
                lambda x, y: x + y,
                l)),
        # split into line_size pieces
        # there is also a grouper recipe: https://docs.python.org/2/library/itertools.html#recipes
        izip(
            *[islice(l, i, None, line_size) for i, l in
              enumerate(
                  tee(output_colors, line_size))])))