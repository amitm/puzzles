"""

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.


Notes:

First solution:

Determine the factors of the number and simplify. Get the correct onesmThen try each combination of digits
if either will get you to the number.

"""
import math

def get_factorials(num):
    factorials = set()
    for i in xrange(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factorials.add(i)
            factorials.add(num / i)
    return factorials

def get_common(numerator, denominator):
    numer = str(numerator)
    denom = str(denominator)
    if numer[1] == denom[1] or numer[0] == denom[0]:
        return False
    elif numer[0] == denom[1]:
        return [int(numer[0]), int(numer[1]), int(denom[0])]
    elif numer[1] == denom[0]:
        return [int(numer[1]), int(numer[0]), int(denom[1])]
    else:
        return False

final_numer = 1
final_denom = 1
for numer in xrange(10, 100):
    for denom in xrange(numer + 1, 100):
        common = get_common(numer, denom)
        if common:
            divisor = max(get_factorials(numer).intersection(get_factorials(denom)))
            simple_numer = numer / divisor
            simple_denom = denom / divisor
            d = 1.0 * common[1] / simple_numer
            if d == int(d) and (1.0 * common[2] / simple_denom) == d:
                final_numer *= simple_numer
                final_denom *= simple_denom


divisor = max(get_factorials(final_numer).intersection(get_factorials(final_denom)))
print final_denom / divisor
