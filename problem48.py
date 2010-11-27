"""

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

"""

total = 0
for x in xrange(1, 1001):
    total += x ** x

print str(total)[-10:]
