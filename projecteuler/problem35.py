"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?

"""

import math

upper_bounds = 1000000

sieve = [1] * upper_bounds

for i in xrange(2, int(math.sqrt(upper_bounds)) + 1):
    if sieve[i] != 1:
        continue
    for j in xrange(i + i, upper_bounds, i):
        sieve[j] = 0
        
circular_primes = 0
for i in xrange(2, upper_bounds):
    if sieve[i] == 1:
        num = str(i)
        circular_prime = True
        for j in xrange(1, len(num)):
            new_num = int(num[j:] + num[:j])
            if sieve[new_num] == 0:
                circular_prime = False
                break
        if circular_prime:
            circular_primes +=1

print circular_primes
        
