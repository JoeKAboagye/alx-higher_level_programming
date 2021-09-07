#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 90 >= ord(i) >= 65:
            print("{:c}".format(i), end="")
    print("")
