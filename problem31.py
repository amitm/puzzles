"""
In England the currency is made up of pound, and pence, p, and there are eight
coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1L1 + 150p + 220p + 15p + 12p + 31p
How many different ways can L2 be made using any number of coins?

"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def num_ways(total, coins):
	if total == 0:
		return 1
	total_ways = 0
	unused_coins = list(coins)
	for coin in coins:
		multiplier = 1
		unused_coins.remove(coin)		
		while True:
			amount = coin * multiplier
			if amount > total:
				break
			else:
				total_ways += num_ways(total - amount, unused_coins)
			multiplier += 1
	return total_ways

print num_ways(200, coins)
			

