"""
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher
text, restores the plain text; for example, 65 XOR 42 = 107, then 
107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text 
message, and the key is made up of random bytes. The user would keep the 
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum
of the ASCII values in the original text.
"""

import sys

if __name__ == "__main__":
    f = open('data/cipher1.txt')
    text = f.read().strip().split(',')
    
    # brute force it
    for a in xrange(97, 123):
        for b in xrange(97, 123):
            for c in xrange(97, 123):
                cipher = [chr(a), chr(b), chr(c)]
                cipher_index = 0
                decrypted = []
                for char in text:
                    if cipher[cipher_index]:
                        decoded = chr(ord(cipher[cipher_index]) ^ int(char))
                    else:
                        decoded = char
                    decrypted.append(decoded)
                    cipher_index = (cipher_index + 1) % 3
                result = ''.join(decrypted)
                if result.find(' the ') != -1:
                    total = 0
                    print sum([ord(i) for i in result])
                    sys.exit()
                    
    