"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1  d10  d100  d1000  d10000  d100000  d1000000

"""

num = 1
total = 0
required_indecies = [1, 10, 100, 1000, 10000, 100000, 1000000]
product = 1

for index in required_indecies:
	while True:
		strnum = str(num)
		length = len(strnum)
		total += length
		diff = total - index
		num += 1
		if diff < length and diff >= 0:
			product *= int(strnum[length - 1 - diff])
			break
			
print product