"""
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with 
British usage.


Notes:

Overall seems like busy work. All you need to calculate is the initial set:
one
two
three
.
.
.
ten
eleven
twelve

After nineteen, everything that comes after the most significant number is 
just reuse.

For example:
twenty-one
twenty-two
one hundred and twenty-two

Solution is to figure out the base set and then just extrapolate, its more
busy work than anything else

"""

# change these to their integer values
base_numbers = ("one", "two", "three", "four", "five", "six", 
                "seven", "eight", "nine", "ten", "eleven", "twelve", 
                "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen")
tens = ("twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety")

total = 0
for n in xrange(1, 1000):
    string = ""
    if n >= 100:
        index = n / 100
        string += base_numbers[index - 1] + "hundredand"
        n -= index * 100
    if n > 19:
        index = n / 10
        string += tens[index - 2]
        n -= index * 10
    if n > 0:
        string += base_numbers[n - 1]
    total += len(string)
    
print total + len("onethousand")