import string


def is_pangram(s):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabets:
        if char not in s.lower():
            return False
    return True
