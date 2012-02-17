"""
A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16  -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

import time

results = {}
def ends_with_eighty_nine(num):
    if num in results:
        return results[num]
    if num == 1:
        return False
    if num == 89:
        return True
    else:
        temp = num
        new_num = 0
        while temp > 0:
            new_num += (temp % 10) ** 2
            temp /= 10
        result = ends_with_eighty_nine(new_num)
        results[num] = result
        return result

if __name__ == '__main__':
    total = 0
    start = time.clock()
    for i in xrange(1, 10000000):
        if ends_with_eighty_nine(i):
            total += 1
        if i % 1000000 == 0:
            print time.clock() - start, i
            start = time.clock()
    print total