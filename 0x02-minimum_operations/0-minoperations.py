#!/usr/bin/python3

def minOperations(n):
    if n <= 0:
        return 0

    operations = 0
    HCharacter = 1
    the_clipboard = 0

    while HCharacter < n:
        if n % HCharacter == 0:
            the_clipboard = HCharacter
            operations += 2
        else:
            the_clipboard += HCharacter
            operations += 1

        HCharacter = the_clipboard

    return operations if HCharacter == n else 0
