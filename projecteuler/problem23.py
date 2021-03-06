"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.

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

def abundant_numbers():
    numbers = set()
    for i in xrange(12, 28124):
        total = sum_divisors(i)
        if total > i:
            numbers.add(i)
    return numbers

numbers = abundant_numbers()
sums = set()
for i in numbers:
    for j in numbers:
        sums.add(i + j)

total = 0
for i in xrange(1, 28124):
    if i not in sums:
        total += i

print total
