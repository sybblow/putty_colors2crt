from __future__ import print_function
from itertools import izip_longest, imap, ifilter
import sys

color2pos = [8, 0, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15]


def putty_import(filename):
    r = imap(
        lambda t: (
            int(t[1][6:]),
            ['%02x' % int(e) for e in t[3].split(',')] + ['00']
        ),
        ifilter(
            lambda t: len(t) > 3,
            imap(
                lambda l: (l.split('"')),
                open(filename, 'r')
            )
        )
    )
    return [(num - 6, c) for num, c in r if num >= 6]


def main():
    filename = sys.argv[1] if len(sys.argv) >= 2 else 'E:\\terminal-sexy.txt'

    output_colors = [None] * 16
    for num, color in putty_import(filename):
        output_colors[color2pos[num]] = color

    group_size = 8
    map(
        print,
        imap(
            lambda l: ' '.join(reduce(list.__add__, l)),
            # a recipe take from "grouper" in this link:
            # https://docs.python.org/2/library/itertools.html#recipes.
            izip_longest(
                *([iter(output_colors)] * group_size)
            )
        )
    )


if __name__ == '__main__':
    main()
