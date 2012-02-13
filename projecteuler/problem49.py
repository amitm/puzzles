"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

for each i in the set
    new_set = permuations(rest of set - i)
    return_set = set()
    for item in set:
        return_set.add(i + item)
    return set
"""

from problem47 import get_sieve

sieve = get_sieve(10000)

def get_permutations(num):
    def _get_permutations_helper(str_num):
        if not str_num:
            return set([""])
        permutations = set()
        for i in xrange(len(str_num)):
            new_num = list(str_num)
            head = new_num.pop(i)
            temp_permutations = _get_permutations_helper(new_num)
            for permutation in temp_permutations:
                permutations.add(head + permutation)
        return permutations
    permutations = []
    str_num = str(num)
    for i in _get_permutations_helper(list(str_num)):
        if len(str(int(i))) == len(str_num):
            permutations.append(int(i))
    permutations.sort()
    return permutations

def remove_composites(items):
    return [i for i in items if sieve[i] == 1]

def get_unusual(items):
    if len(items) < 3:
        return False
    for i in xrange(len(items) - 2):
        for j in xrange(i + 1, len(items) - 1):
            final_item = 2 * items[j] - items[i]
            if final_item in items:
                return str(items[i]) + str(items[j]) + str(final_item)

if __name__ == "__main__":    
    unusual_set = set()
    for i in xrange(1000, 9999):
        if sieve[i] == 1:
            unusual = get_unusual(remove_composites(get_permutations(i)))
            if unusual:
                unusual_set.add(unusual)
    print unusual_set

    
