"""
Starting with 1 and spiralling anticlockwise in the following way, a square 
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13  62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""
from math import sqrt
from problem47 import get_sieve

sieve = get_sieve(10000000)

def is_prime(num):
    if num < len(sieve):
        return sieve[num] == 1
    limit = int(sqrt(num))
    if limit > len(sieve):
        print "Error: sieve not large enough"
        return False
    for i in xrange(2, limit):
        if sieve[i] == 1 and num % i == 0:
            return False
    return True

def get_num_primes(side_length):
    number = side_length ** 2
    i = 0
    primes = 0
    while i < 4:
        if i != 0 and is_prime(number):
            primes += 1
        number -= (side_length - 1)
        i += 1
    return primes
        
    
if __name__ == "__main__":
    percent = 100
    side_length = 1
    primes = 0
    while percent >= .10:
        side_length += 2
        primes += get_num_primes(side_length)
        percent = 1.0  * primes / (2 * side_length - 1)
    print side_length