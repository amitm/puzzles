"""
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382 ^ 518061 < 519432 ^ 525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line, determine
which line number has the greatest numerical value.
NOTE: The first two lines in the file represent the numbers in the example
given above.
"""

def compare(a, b):
    return cmp(a[0], b[0] ** (1.0 * b[1] / a[1]))

if __name__ == "__main__":
    f = open("data/base_exp.txt")
    numbers = []
    for line in f:
        nums = line.strip().split(",")
        numbers.append((int(nums[0]), int(nums[1])))
    largest = numbers[0]
    line = 0
    for i in xrange(1, len(numbers)):
        if compare(largest, numbers[i]) == -1:
            line = i
            largest = numbers[i]
    print line + 1