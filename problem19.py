"""
You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

"""

start_year = 1901
end_year = 2000

first_of_month_days = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
was_leap_year = False
num_sundays = 0

for year in xrange(start_year, end_year + 1):
    left = None
    right = None
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        left = map(lambda x: (x + 1) % 7, first_of_month_days[:2])
        right = map(lambda x: (x + 2) % 7, first_of_month_days[2:])
        was_leap_year = True
    else:
        inc = 2 if was_leap_year else 1
        left = map(lambda x: (x + inc) % 7, first_of_month_days[:2])
        right = map(lambda x: (x + 1) % 7, first_of_month_days[2:])
        was_leap_year = False
    left.extend(right)
    first_of_month_days = left
    num_sundays += first_of_month_days.count(0)

print num_sundays