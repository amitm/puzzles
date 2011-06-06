"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

Thoughts:
1. The total number of digits used needs to be 9 that limits the size of the operands

"""

def is_pandigital(a, b, c):
	str_a = str(a)
	str_b = str(b)
	str_c = str(c)
#	if len(str_a) + len(str_b) + len(str_c) != 9:
#		return False
	digits = [0] * 10
	for digit in str_a + str_b + str_c:
		int_digit = int(digit)
		if int_digit == 0 or digits[int_digit] == 1:
			return False
		digits[int(digit)] = 1
	return True

products = []
total = 0

for i in xrange(1, 10):
	for j in xrange(1000, 10000):
		c = i * j
		if len(str(c)) > 4:
			break
		if is_pandigital(i, j, c):
			print i, j, c
			if c not in products:
				products.append(c)
				total += c

for i in xrange(10, 100):
	for j in xrange(100, 1000):
		c = i * j
		if len(str(c)) > 4:
			break
		if is_pandigital(i, j, c):
			print i, j, c
			if c not in products:
				products.append(c)
				total += c
print total
