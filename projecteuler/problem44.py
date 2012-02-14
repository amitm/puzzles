"""
Pentagonal numbers are generated by the formula, Pn=n(3n - 1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference is pentagonal and D = |Pk  Pj| is minimised; what is the value of
D?
"""

import sys
from problem45 import is_pentagonal


def main():
    pentagonals = [i * (3 * i - 1) / 2 for i in xrange(1, 10000)]
    min_d = sys.maxint
    for i in xrange(len(pentagonals)):
        for j in xrange(i + 1, len(pentagonals)):
            s = pentagonals[i] + pentagonals[j]
            d = pentagonals[j] - pentagonals[i]
            if is_pentagonal(s) and is_pentagonal(d):
                return d

if __name__ == "__main__":
    print main()