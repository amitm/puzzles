"""

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
5, 6, 7, 8 and 9?

"""

import math

available_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

limit = 1000000
total = 0
num = []

while len(available_numbers) > 0:
    size = len(available_numbers)
    factorial = math.factorial(size - 1)
    index = -1
    for i in xrange(1, size):
        if total + i * factorial >= limit:
            index = (i - 1)
        elif i == size - 1:
            index = i
        if index != -1:
            total += index * factorial
            print "add"
            break
    print size, index, total, factorial, index * factorial 
    num.append(available_numbers.pop(index))

print num