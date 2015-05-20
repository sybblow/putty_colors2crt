from __future__ import print_function
from itertools import izip_longest, imap
import sys


color2pos = [8, 0, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]


filename = sys.argv[1] if len(sys.argv) >= 2 else 'E:\\terminal-sexy.txt'
r = imap(
    lambda t: (
        int(t[1][6:]),
        ['%02x' % int(e) for e in t[3].split(',')] + ['00']
    ),
    imap(
        lambda l: (l.split('"')),
        open(filename, 'r')
    )
)
r = [(color2pos[num - 6], c) for num, c in r if num >= 6]

output_colors = [None] * 16
for pos, c in r:
    output_colors[pos] = c

group_size = 8
map(
    print,
    imap(
        lambda l: ' '.join(
            reduce(
                lambda x, y: x + y,
                l
            )
        ),
        # a recipe take from "grouper" in this link:
        # https://docs.python.org/2/library/itertools.html#recipes.
        izip_longest(
            *([iter(output_colors)] * group_size)
        )
    )
)