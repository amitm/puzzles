"""
Euler's Totient function f(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n. For
example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to
nine, f(9)=6.

n	Relatively Prime f(n)	n/f(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5

It can be seen that n=6 produces a maximum n/f(n) for n <= 10. Find the value of
n <= 1,000,000 for which n/f(n) is a maximum.

if gcd(m, n) = 1 then phi(mn) = phi(m) * phi(n)
"""

import time
import sys
from problem47 import get_sieve


sieve = get_sieve(1000001)
solved_factors = {}
    
def is_prime(num):
    return sieve[num] == 1

def get_next_prime(num):
    for i in xrange(num + 1, len(sieve)):
        if sieve[i] == 1:
            return i
    
def get_prime_factors(num):
    prime_divisor = 2
    factored_num = num
    factors = []
    while True:
        if factored_num in solved_factors:
            factors += solved_factors[factored_num]
            break
        elif is_prime(factored_num):
            factors.append(factored_num)
            break
        elif factored_num % prime_divisor == 0:
            factors.append(prime_divisor)
            factored_num = factored_num / prime_divisor
        else:
            prime_divisor = get_next_prime(prime_divisor)
    solved_factors[num] = factors
    return factors

def get_totient(n):
    if is_prime(n):
        return n - 1
    factors = get_prime_factors(n)
    
    totients = []
    for num in set(factors):
        total = 0
        for i in factors:
            if i == num:
                total += 1
        limit = num ** total
        totients.append(limit - limit / num)
    return reduce(lambda x, y: x * y, totients)
        
    
    
if __name__ == "__main__":
    start = time.time()
    maximum = 0
    n = 0

    for i in xrange(2, 1000001):
        totient = get_totient(i)
        val = 1.0 * i / totient
        if val > maximum:
            n = i
            maximum = val
    print n, time.time() - start
        
