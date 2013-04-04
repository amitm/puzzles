"""
By replacing the 1st digit of *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""

from problem47 import get_sieve


def replace_digits(num):
    str_num = str(num)
    for i in xrange(10):
        char = str(i)
        if char in str_num:
            for j in xrange(10):
                if j != i:
                    yield int(str_num.replace(char, str(j)))


def main():
    size = 1000000
    sieve = get_sieve(size)
    seen = set([])
    required_family_size = 8
    smallest = size
    for num in xrange(size):
        if sieve[num] == 0 or num in seen:
            continue
        str_num = str(num)
        for i in xrange(10):
            char = str(i)
            if sieve[num] == 1:
                family = [num]
                seen.add(num)
            else:
                family = []
            if char in str_num:
                for j in xrange(10):
                    if j != i:
                        new_num = int(str_num.replace(char, str(j)))
                        if len(str(new_num)) != len(str_num):
                            continue
                        if sieve[new_num] == 1:
                            family.append(new_num)
                            seen.add(new_num)
                            if len(family) >= required_family_size:
                                family.sort()
                                if family[0] < smallest:
                                    smallest = family[0]
    print smallest


if __name__ == '__main__':
    main()
