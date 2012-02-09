"""
A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the
file so as to determine the shortest possible secret passcode of unknown
length.
"""

def in_any_set(i, sets):
    for a_set in sets:
        if i in a_set:
            return True
    return False

if __name__ == "__main__":
    keylog_file = open('data/keylog.txt')
    pre_numbers = [set() for i in xrange(10)]
    
    for line in keylog_file:
        num_0 = int(line[0])
        num_1 = int(line[1])
        num_2 = int(line[2])
        
        pre_numbers[num_1].add(num_0)
        
        pre_numbers[num_2].add(num_0)
        pre_numbers[num_2].add(num_1)
    
    set_lengths = []
    for i in xrange(10):
        if len(pre_numbers[i]) > 0 or in_any_set(i, pre_numbers):
            set_lengths.append((i, len(pre_numbers[i])))
    set_lengths = sorted(set_lengths, lambda x,y: cmp(x[1], y[1]))
    print ''.join(["%d" % i[0] for i in set_lengths])