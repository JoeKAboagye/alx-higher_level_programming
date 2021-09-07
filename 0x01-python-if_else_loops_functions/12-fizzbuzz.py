#!/usr/bin/python3
"""
This prints the numbers from 1 to 100
multiples of three print Fizz
instead of the number and
multiples of five print Buzz
numbers which are multiples of both
three and five print FizzBuzz
"""


def fizzbuzz():
    for num in range(1, 101):
        str = ""
        if num % 3 == 0:
            str += "Fizz"
        if num % 5 == 0:
            str += "Buzz"
        if num % 5 != 0 and num % 3 != 0:
            str += str(num)
        print("{} ".format(str), end="")
