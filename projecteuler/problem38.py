"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

def is_pandigital(products):
	digits = [0] * 10
	for digit in products:
		int_digit = int(digit)
		if int_digit == 0 or digits[int_digit] == 1:
			return False
		digits[int(digit)] = 1
	return True

largest = 0
for i in xrange(1, 10000):
	j = 1
	products = ""
	while True:
		products += str(i * j)
		if len(products) == 9 and is_pandigital(products):
			print i, products
			num = int(products)
			if num > largest:
				largest = num
			break
		elif (len(products) > 9):
			break
		j += 1

print largest
