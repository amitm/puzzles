"""

Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2  79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.

b has to be a prime for n = 0 to work b = {all primes < 1000}

need to find the max number so we can generate the sieve to be that big

"""
import math

upper_bounds = 20000
sieve = [1] * upper_bounds

# get the first 1000 primes
for i in xrange(2, int(math.sqrt(upper_bounds)) + 1):
    if sieve[i] != 1:
        continue
    for j in xrange(i + i, upper_bounds, i):
        sieve[j] = 0

b_values = set()
primes = set()
for i in xrange(2, upper_bounds):
    if sieve[i] == 1:
        primes.add(i)
        if i < 1000:
            b_values.add(i)

max_consecutive = 0
max_a = 0
max_b = 0

for a in xrange(-999, 1000):
    for b in b_values:
        n = 1
        consecutive = 1
        while True:
            result = n ** 2 + a * n + b
            if result < 2:
                break
            elif result > upper_bounds:
                print result
                break
            elif result not in primes:
                break
            else:
                consecutive += 1
            n += 1
        if consecutive > max_consecutive:
            max_consecutive = consecutive
            max_a = a
            max_b = b

print max_a, max_b, max_a * max_b