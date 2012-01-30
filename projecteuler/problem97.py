"""
The first known prime found to exceed one million digits was discovered in 
1999, and is a Mersenne prime of the form 269725931; it contains exactly 
2,098,960 digits. Subsequently other Mersenne primes, of the form 2p1, have
been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433 * 2**7830457 + 1.

Find the last ten digits of this prime number.

last digit is 2, 4, 8 or 6

power % 4 == 0, then its 6
(power + 1) % 4 == 0 then it is 8
(power + 2) % 4 == 0 then it is 4
(power + 3) % 4 == 0 then it is 2

7830457 + 3 % 4 == 0, so 6 is the last digit

2
4
9
9
8
6
3
7
4
8
7
5
0
0
1
3
6
2
5
1

so there needs to be a way to do this automatcially
1. create a list of powers
2. choose the digit you are working on
3. find the pattern
4. use the pattern to find the number that would be used for that particular item

Need to throw away stuff at the beginning if you don't find a pattern
throw away stuff at the end too

it is a pattern if the item we find next is the same as the start of the
pattern and the length of the pattern are the same, have to retest for pattern
until the correct mutliple to the end of the string

"""


def is_pattern(pattern, numbers):
    for i in xrange(0, len(numbers), len(pattern)):
        end = i + len(pattern)
        if end < len(numbers) and pattern != numbers[i:end]:
            return False
    return True

def get_pattern(powers, digit):
    pattern_start = 0
    digits = []
    for i in powers:
        if len(i) < digit:
            pattern_start += 1
            digits.append('')
        else:
            digits.append(i[len(i) - digit])
    for pattern_start in xrange(pattern_start, len(digits) / 4):
        for i in xrange(pattern_start + 1, len(digits) / 2):
            # the intial digit is the same, there might be a pattern
            if digits[i] == digits[pattern_start]:
                if is_pattern(digits[pattern_start:i], digits[i:]):
                    return (pattern_start, digits[pattern_start:i])
    return None

def get_digit(power, pattern_start, pattern):
    return pattern[(power - pattern_start) % len(pattern)]

powers = [str(2 ** i) for i in xrange(100000)]

digits = []
for i in xrange(1, 7):
    pattern_start, pattern = get_pattern(powers, i)
    digits.insert(0, get_digit(28433, pattern_start, pattern))

last_digits = str(28433 * int(''.join(digits)))
print last_digits[len(last_digits) - 10:len(last_digits)]

        
            
            



