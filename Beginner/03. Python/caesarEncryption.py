# Problem Statement
# Get program for caesar cipher in python for encryption and decryption.
# What is Caesar Cipher?
# It is one of the simplest encryption technique in which each character 
# in plain text is replaced by a character some fixed number of positions down to it.
# For example, if key is 3 then we have to replace character by another 
# character that is 3 position down to it. Like A will be replaced by D, C will be replaced by F and so on.

# solution
alpha = list("abcdefghijklmnopqrstuvwxyz")

def freq(ch: chr, s: str) -> int:
    return sum([1 for _ in s if _.lower() == ch.lower()])


def odd(n: int) -> bool:
    return n % 2 == 1


def encrypt_char(ch: chr, string: str, key: int):
    ch = ch.lower()
    return {True: alpha[(alpha.index(ch) - key) % 26],
            False: alpha[(alpha.index(ch) + key) % 26],
            }[odd(freq(ch,string))]


def encrypt_string(string: str, key: int):
    result = ""
    for i in string:
        result += encrypt_char(i, string, key)
    return result


print(encrypt_string("hello", 28))
