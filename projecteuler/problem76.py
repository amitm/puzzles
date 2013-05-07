"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?
"""

def test():
  print "Hello World"


if __name__ == '__main__':
    # fairly simple dynamic programming solution
    num = 100
    sums = [1] * (num + 1)
    for i in xrange(2, len(sums)):
        for j in xrange(i, len(sums)):
            sums[j] += sums[j - i]
    # since it has to the be the sum of at least two
    print sums[num] - 1
