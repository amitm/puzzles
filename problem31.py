"""
In England the currency is made up of pound, and pence, p, and there are eight
coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1L1 + 150p + 220p + 15p + 12p + 31p
How many different ways can L2 be made using any number of coins?

1 way to make 1p (1 x 1p)
2 ways to make 2p (2 x 1p, 1 x 2p)

To make 3p:
2 ways to make 2p x 1 way to make 1p = 2 ways

To make 4p:

4 x 1p
2 x 1p + 1 x 2p
2 x 2p

3 ways


To make 5p:

1 x 5p
2 x 2p + 1p
1 x 1p + 3 x 1p
5 x 1p

To Make 6p:
1 x 5p + 1 x 1p
3 x 2p
2 x 2p + 2 x 1p
1 x 2p + 4 x 1p
6 x 1p

To Make 10p:
10
1 x 5p + 5 x 1

"""

previous = 2
coins = [2, 5, 10, 20, 50, 100, 200]

for i in xrange(3, 201):
	total = previous
	for j in coins:
		remainder = i % j
		if remainder != i and (remainder in coins or remainder == 0):
			total += 1
	print i, total
	previous = total

