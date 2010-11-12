"""
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67, is the same challenge with a
triangle containing one-hundred rows; it cannot be solved by brute force, and
requires a clever method! ;o)


Note:

Name of the game here is elimination. The algorithm cannot solve by brute 
force so it needs to recognize which route could possibly the biggest.
How do you determine which routes to get rid of?

The issue here is that you could just choose the biggest option on each
step but you could miss a large number because your route wont use it.


There might also be significant savings by saving the total of
the routes below and reuing numbers.

Divide and conquer. Since the only correct decision you can make is
of a triangle of 2 rows, start from the bottom and do that.  Then bubble
The numbers up:

   3
  7 4
 2 4 6
8 5 9 3

Gives you these options:

 2    4    6
8 5  5 9  9 3

Which then turns into for the next row:

  07      04
10  13  13  15


THETA(n^2) time based on the number of rows

running_time = 2*SUM(i) where i = 1 to rows

THETA(n^2)
"""


tree = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

for i in xrange(len(tree) - 2, -1, -1):
    current_row = tree[i]
    deeper_row = tree[i + 1]
    for j in xrange(0, len(current_row)):
        a = deeper_row[j]
        b = deeper_row[j + 1]
        current_row[j] += a if a > b else b

print tree[0][0]