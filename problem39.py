"""

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?

a + b + c = x
b = x - a - c

a ^ 2 + b ^ 2 = c ^ 2
a ^ 2 + (x - a - c) ^ 2 = c ^ 2
a ^ 2 + (x - a) ^ 2 - 2 * (x - a) * c + c ^ 2 = c ^ 2
a ^ 2 + (x - a) ^ 2 - 2 * (x - a) * c = 0
a ^ 2 + (x - a) ^ 2 = 2 * (x - a) * c
(a ^ 2 + (x - a) ^ 2) / (2 * (x - a)) = c

a = 20
x = 120

20 + 100 ^ 2 - 2 * 100 * c = 0

10400 = 200 * c

"""

max_solutions = 0
max_p = 0
c_list = []

for p in xrange(1, 1000):
    solutions = set()
    for a in xrange(1, p / 3):
        c = (1.0 * a ** 2 + (p - a) ** 2) / (2 * (p - a))
        if c == int(c) and c not in solutions:
            solutions.add(c)
    if len(solutions) > max_solutions:
        max_solutions = len(solutions)
        max_p = p

print max_p