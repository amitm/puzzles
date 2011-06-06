"""

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

"""
import math

def generate_prime_checker(upper_bounds):
	sieve = [1] * upper_bounds

	# get the first 1000 primes
	for i in xrange(2, int(math.sqrt(upper_bounds)) + 1):
	    if sieve[i] != 1:
	        continue
	    for j in xrange(i + i, upper_bounds, i):
	        sieve[j] = 0

	primes = []
	for i in xrange(2, upper_bounds):
	    if sieve[i] == 1:
	        primes.append(i)
	def is_prime(num):
		if num < upper_bounds:
			return sieve[num] == 1
		root = math.sqrt(num)
		for j in primes:
			if j > root:
				return True
			if num % j == 0:
				return False
		return True
	return is_prime

is_prime = generate_prime_checker(32000)
pandigitals = [["1"]]

for i in xrange(1, 9):
	current_pandigitals = []
	pandigitals.append(current_pandigitals)
	previous_pandigitals = pandigitals[i - 1]
	current_digit = str(i + 1)
	for num in previous_pandigitals:
		for j in xrange(i + 1):
			current_pandigitals.append(num[:j] + current_digit + num[j:])


largest = 0
for i in xrange(8, -1, -1):
    current_pandigitals = pandigitals[i]
    for j in current_pandigitals:
        num = int(j)
        if num > largest and is_prime(num):
            largest = num
    if largest != 0:
        print largest
        break