"""

A googol (10100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b  100, what is the
maximum digital sum?

"""

largest = 0
for i in xrange(100):
    for j in xrange(100):
        c = str(i ** j)
        total = 0
        for digit in c:
            total += int(digit)
        largest = max(largest, total) 
        
print largest
        