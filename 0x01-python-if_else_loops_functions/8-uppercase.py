#!/usr/bin/python3
"""
This prints a string in uppercase
"""


def uppercase(str):
    for c in str:
        if ord(c) >= 95 and ord(c) <= 124:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
