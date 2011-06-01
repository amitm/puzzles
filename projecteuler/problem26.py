"""

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.


Amit:
Once you find yourself starting back at the same problem you were at initially
you know that you have restarted. The real question is to find out if you every equal
something that you had before and then tag it

"""

def cycle_len(number):
	numerator = 1
	while number > numerator:
		numerator *= 10
	previous_numerators = []
	i = 0
	while numerator != 0:
		result = numerator / number
		numerator = numerator % number
		i += 1
		try:
			return len(previous_numerators) - previous_numerators.index(numerator)
		except ValueError:
			previous_numerators.append(numerator)
			numerator *= 10
	return 0
	
longest = 0
d = 0
for i in xrange(1, 1000):
	cycle = cycle_len(i)
	if longest < cycle:
		longest = cycle
		d = i

print d