"""

The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle 
words?

"""
import math
import sys

def word_score(word):
    word_score = 0
    for i in word:
        word_score += (ord(i) - 64)
    return word_score

def is_triangle(score):
    total = math.sqrt(1 + 4 * 2 * score)
    total_int = int(total)
    if total_int == total and total_int % 2 == 1:
        return True
    return False
    
total = 0    
filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
    print line
    if (is_triangle(word_score(line.strip()))):
        total += 1

print total