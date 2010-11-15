"""
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

24: 1, 2, 3, 4, 6, 8, 12

12: 1, 2, 3, 4, 6

"""

import math

def sum_divisors(number):
    sqrt = math.sqrt(number)
    sqrt_int = int(math.ceil(sqrt))
    total = 1
    if number == 1:
        return total
    for i in xrange(2, sqrt_int):
        if number % i == 0:
            total += i
            total += number / i
    if sqrt_int == sqrt:
        total += sqrt_int
    return total

sums = []
for i in xrange(1, 10000):
    sums.append(sum_divisors(i))

amicable_numbers = set()
for i in xrange(0, 9999):
    total = sums[i]
    if total < 10000:
        if sums[total - 1] == (i + 1) and i + 1 != total:
            amicable_numbers.add(i + 1)
            amicable_numbers.add(total)
            
print reduce(lambda x, y: x+y, amicable_numbers)
            

