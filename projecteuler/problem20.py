"""

n! means n  (n  1)  ...  3  2  1

Find the sum of the digits in the number 100!

"""


import math

total = 0
for i in str(math.factorial(100)): 
    total += int(i) 
print total

