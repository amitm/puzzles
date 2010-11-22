"""
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?

"""

n = 1001
upper_right_numbers = [1]
total = 1
for i in xrange(1, (n - 1) / 2 + 1):
    multiplier = 8 * i
    number = upper_right_numbers[i - 1] + multiplier
    upper_right_numbers.append(number)
    step_size = multiplier / 4
    total += number + (number - step_size) +\
            (number - 2 * step_size) + (number - 3 * step_size)
print total
