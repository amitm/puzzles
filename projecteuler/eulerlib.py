def is_palindrome(number):
    number = str(number)
    length = len(number)
    for i in xrange(length / 2):
        if number[i] != number[length - i - 1]:
            return False
    return True