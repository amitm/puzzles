"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?

"""

import sys

filename = sys.argv[1]
f = open(filename, 'r')

data = f.read()
names = data.replace('"', "").split(",")
names.sort()

i = 1
total = 0
for name in names:
    total += i * reduce(lambda x, y: x + y, map(lambda x: ord(x) - 64, name))
    i += 1

print total
