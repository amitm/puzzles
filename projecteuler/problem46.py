"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?

"""

import math
from problem47 import get_sieve

max_num = 100000
sieve = get_sieve(max_num)

def get_smaller_prime(num):
    for i in xrange(num - 1, 0, -1):
        if sieve[i] == 1:
            return i
    # throw an error
    return 0

def is_goldbach(num):
    prime = get_smaller_prime(num)
    while prime > 1:
        new_num = num - prime
        if new_num % 2 == 0:
            sqrt = math.sqrt(new_num / 2)
            if sqrt == int(sqrt):
                return True
        prime = get_smaller_prime(prime)
    return False

if __name__ == "__main__":
    for i in xrange(3, max_num, 2):
        if sieve[i] == 0 and not is_goldbach(i):
            print i
            break
    