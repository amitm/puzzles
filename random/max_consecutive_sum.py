# Problem of the week - Max Consecutive Sum

# The problem: Find the maximum sum possible from picking a contiguous
# subsequence of an array.

# [-1, 5, 6, -2, 20, -50, 4]
# What is the largest sum of contiguous elements available in this list?

# In the example above, the maximum sum would be 29:
# [-1, 5, 6, -2, 20, -50, 4], because (5 + 6 - 2 + 20 = 29).
# End one element later and you'll go negative. Start one element earlier and
# you'll subtract one.

#
# Thoughts
# Hold on to the max sum so far and keep adding unless it goes <= 0


def max_consecutive_sum(nums):
    max_sum = nums[0]
    current_sum = 0

    for i in nums:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum <= 0:
            current_sum = 0

    return max_sum

if __name__ == '__main__':
    print max_consecutive_sum([-1, 5, -1, -2, 20, -50, 4])
