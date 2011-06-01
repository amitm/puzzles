"""

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

"""

def is_palindrome(number):
    number = str(number)
    length = len(number)
    for i in xrange(length / 2):
        if number[i] != number[length - i - 1]:
            return False
    return True

def to_binary(number):
    binary_str = ""
    while (number > 0):
        binary_str = str(number % 2) + binary_str
        number /= 2
    return binary_str
    
total = 0
for i in xrange(1, 1000000, 2):
    if is_palindrome(i) and is_palindrome(to_binary(i)):
        total += i

print total
