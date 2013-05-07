# Given an array of integers, find all combinations of n values in the array
# such that their sum is 0

# brute force and find all combinations > than one


def find_combinations(items, num):
    if num == 1:
        return [[i] for i in items]
    result = []
    for i in xrange(len(items) - (num - 1)):
        combinations = find_combinations(items[i + 1:], num - 1)
        for c in combinations:
            result.append([items[i]] + c)
    return result


def get_permutations(items):
    if len(items) == 1:
        return [items]
    permutations = get_permutations(items[1:])
    front = items[0]
    results = []
    for p in permutations:
        for i in xrange(len(p) + 1):
            results.append(p[:i] + [front] + p[i:])
    return results

if __name__ == '__main__':
    #items = [1, -2, 3, 4, -2]
    #total = 0
    #for i in xrange(2, len(items) + 1):
    #    combinations = find_combinations(items, i)
    #    for c in combinations:
    #        if sum(c) == 0:
    #            total += 1
    #print total
    print get_permutations([1, 2, 3, 4])
