"""
Consider the fraction, n/d, where n and d are positive integers. If nd and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of 
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d  1,000,000 in ascending 
order of size, find the numerator of the fraction immediately to the left of 3/7.

***
All pairs of coprime numbers m,n can be generated in a parent-3 children-9 
grandchildren... family tree starting from (2,1) (for even-odd or odd-even
pairs) or from (3,1) (for odd-odd pairs),[5] with three branches from each node.
The branches are generated as follows:

Branch 1: mnext = 2m - n, and nnext = m
Branch 2: mnext = 2m + n, and nnext = m
Branch 3: mnext = m + 2n, and nnext = n

"""

import sys
import time

def get_gcd(a, b):
    while b != 0:
        b, a = a % b, b
    return a
    
def is_coprime(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return False
    return get_gcd(a, b) == 1

def get_potential_answers(num):
    upper_limit = 3.0 / 7.0
    lower_limit = 0.42856
    
    start = int(upper_limit * num) + 1
    while True:
        value = 1.0 * start / num
        if value < lower_limit:
            break
        if value < upper_limit and is_coprime(start, num):
            return (start, num, value)
        
        start -= 1
    return None
    
if __name__ == "__main__":
    answers = []
    start = time.time()
    
    for i in xrange(2, 1000001):
        answer = get_potential_answers(i)
        if answer:
            answers.append(answer)
    answers = sorted(answers, lambda x, y: cmp(x[2], y[2]))
    print answers[len(answers) - 1][0]
            
