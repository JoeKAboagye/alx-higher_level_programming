#!/usr/bin/python3
"""
This prints a string in uppercase
"""

def uppercase(str):
    for i in str:
        if 122 >= ord(i) >= 97:
            i = (ord(i) - 32)
        else:
            i = ord(i)
        print("{:c}".format(i), end="")
    print("")
