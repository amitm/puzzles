import math

upper_bounds = 1000000

sieve = [1] * upper_bounds

sieve[1] = 0
for i in xrange(2, int(math.sqrt(upper_bounds)) + 1):
    if sieve[i] != 1:
        continue
    for j in xrange(i + i, upper_bounds, i):
        sieve[j] = 0

primes = []
for i in xrange(10, len(sieve)):
    if sieve[i] == 0:
        continue
    strnum = str(i)
    is_prime = True
    for j in xrange(1, len(strnum)):
        strnum = strnum[1:]
        if sieve[int(strnum)] == 0:
            is_prime = False
            break
    if is_prime:
        strnum = str(i)        
        for j in xrange(1, len(strnum)):
            strnum = strnum[:-1]
            if sieve[int(strnum)] == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(i)

print sum(primes)