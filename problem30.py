"""
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

"""

import math
import time

powers = (0, 1, 32, math.pow(3, 5), math.pow(4, 5), math.pow(5, 5), 
          math.pow(6, 5), math.pow(7, 5), math.pow(8, 5), math.pow(9, 5))

def sum_of_digits(number):
    digits = str(number)
    total = 0
    for i in digits:
        total += powers[int(i)]

start_time = time.clock()

for i in xrange(2, 10000000):
    if i == sum_of_digits(i):
        print i
    
print time.clock() - start_time