"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

**
Since the prime has to be below one-million two consectuive numbers have to
equal one million ~499,999 + 500,000 so the highest prime needed is below
500,000

"""
import math

def get_primes(upper_bounds):
    sieve = [1] * upper_bounds
    for i in xrange(2, int(math.sqrt(upper_bounds)) + 1):
        if sieve[i] == 1:
            for j in xrange(i + i, upper_bounds, i):
                sieve[j] = 0
    
    # we choose a list because we need it in order
    primes = []
    for i in xrange(2, upper_bounds):
        if sieve[i] == 1:
            primes.append(i)
    return primes
            
def sum_length(number, primes):
    for start in xrange(len(primes)):
        if primes[start] > number / 2:
            return 0
        prime_sum = 0
        length = 0
        for i in xrange(start, len(primes)):
            prime_sum += primes[i]
            length += 1
            if prime_sum > number:
                break
            elif prime_sum == number:
                return length
            
    

if __name__ == "__main__":
    primes = get_primes(1000000)
    reversed_primes = list(primes)
    reversed_primes.reverse()
    answer = 0
    length = 0
    for prime in reversed_primes:
        prime_sum_length = sum_length(prime, primes)
        if prime_sum_length > length:
            answer = prime
            length = prime_sum_length
            print answer, length