"""
The first known prime found to exceed one million digits was discovered in 
1999, and is a Mersenne prime of the form 269725931; it contains exactly 
2,098,960 digits. Subsequently other Mersenne primes, of the form 2p1, have
been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433 * 2**7830457 + 1.

Find the last ten digits of this prime number.

Use modular exponentiation

Since (a x b) mod m = (a x (b mod m)) mod m, you can find the solution
iteratively

We want to find the last few digits of
2 ^ 7830457 

So we do:
2 ** 7830457 % 10000000000

2 mod 10000000000 = c

"""


def modular_pow(base, exponent, modulo):
    c = 1
    for i in xrange(exponent):
        c = (base * c) % modulo
    return c

if __name__ == '__main__':
    result = str(28433 * modular_pow(2, 7830457, 10000000000) + 1)
    print result[len(result) - 10:]

