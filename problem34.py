"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

import math

factorials = [math.factorial(x) for x in xrange(0, 10)]

def curious(digits, length, number, total):
    if length == len(digits):
        if total == number:
            print number
            return number
        return 0
    current = 0
    max_number = number
    for i in xrange(0, length - len(digits)):
        max_number += 9 * (10 ** i)
    curious_sum = 0
    for i in factorials:
        if i <= max_number:
            new_number = number + current * (10 ** (length - len(digits) - 1))
            curious_sum += curious(digits + [current], length, 
                                   new_number, total + i)
        else:
            break
        current += 1
    return curious_sum

curious_sum = 0
# since upper bound is 9999999 (7 * 9!)
for j in xrange(2, 8):
    for i in xrange(1, 10):
        curious_sum += curious([i], j, i * 10 ** (j - 1), factorials[i])
print curious_sum