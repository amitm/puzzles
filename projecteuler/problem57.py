"""
It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth 
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
"""

def get_expansion(iteration):
    def get_expansion_helper(n, starting_n):
        if n == 0:
            return 2, 1
        else:
            # flip because of the 1 / last iteration
            denominator, numerator = get_expansion_helper(n - 1, starting_n)
            # add the 1 + num/denom
            numerator += (denominator if n == starting_n else denominator * 2)
            return numerator, denominator
    return get_expansion_helper(iteration, iteration)

# create an iter because stack recursion was too deep with the recursive
# solution. This can be fixed with an update to stack size, but wanted 
# to see the iterable way to do it
def get_expansion_iter(iteration):
    n = iteration
    numerator = 2
    denominator = 1
    while n > 1:
        numerator, denominator = denominator, numerator
        numerator += denominator * 2
        n -= 1
    numerator, denominator = denominator, numerator
    numerator += denominator
    return numerator, denominator
    
if __name__ == "__main__":
    total = 0
    for i in xrange(1, 1001):
        num, denom = get_expansion_iter(i)
        if len(str(num)) > len(str(denom)):
            total += 1
    print total