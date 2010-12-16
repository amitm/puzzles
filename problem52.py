"""
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.

"""


def to_sorted_array(num):
    array = []
    while num > 0:
        array.append(num % 10)
        num /= 10
    array.sort()
    return array

def make_compare(num):
    num_array = to_sorted_array(num)
    return lambda x: to_sorted_array(x * num) == num_array
        

def sum_of_digits(num):
    num = str(num)
    total = 0
    for i in xrange(len(num)):
        total += int(num[i])
    print num, total
    return total

i = 10
while True:
    compare = make_compare(i)
    if compare(2) and compare(3) and compare(4) and compare(5) and compare(6):
        print i
        break
    i += 1
