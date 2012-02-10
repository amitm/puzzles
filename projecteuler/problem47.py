"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2 * 7 * 23
645 = 3 * 5 * 43
646 = 2^2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?


You need to just start dividing by primes until it doesnt work and go on
"""
import math

def get_sieve(upper_bounds):
    sieve = [1] * upper_bounds
    for i in xrange(2, int(math.sqrt(upper_bounds)) + 1):
        if sieve[i] == 1:
            for j in xrange(i + i, upper_bounds, i):
                sieve[j] = 0
    return sieve

max_num = 1000000
sieve = get_sieve(max_num)

def is_prime(num):
    return sieve[num] == 1

def get_next_prime(num):
    for i in xrange(num + 1, len(sieve)):
        if sieve[i] == 1:
            return i
    # throw an error

def get_unique_prime_factorizer():
    solved_factors = {}
    
    def get_unique_prime_factors(num):
        prime_divisor = 2
        factored_num = num
        factors = set()
        while True:
            if factored_num in solved_factors:
                factors = factors.union(solved_factors[factored_num])
                break
            elif is_prime(factored_num):
                factors.add(factored_num)
                break
            elif factored_num % prime_divisor == 0:
                factors.add(prime_divisor)
                factored_num = factored_num / prime_divisor
            else:
                prime_divisor = get_next_prime(prime_divisor)
        solved_factors[num] = factors
        return factors
    
    return get_unique_prime_factors

def main():
    consecutive = []
    required_len = 4
    get_unique_prime_factors = get_unique_prime_factorizer()
    for i in xrange(max_num):
        if len(get_unique_prime_factors(i)) == required_len:
            consecutive.append(i)
            if len(consecutive) == required_len:
                break
        else:
            consecutive = []
    return consecutive[0] if consecutive else None

if __name__ == "__main__":
    print main()
    
    