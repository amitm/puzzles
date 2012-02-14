"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


if __name__ == "__main__":
    answer = 1
    for i in xrange(100):
        j = 2
        while True:
            digits = len(str(j ** i))            
            if digits > i:
                break
            if digits == i:
                answer += 1
            j += 1
    print answer