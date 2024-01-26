#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = "Last digit of "
if number < 0:
    digit = number % -10
else:
    digit = number % 10

if digit > 5:
    print("{}{} is {} and is greater than 5".format(st, number, digit))
elif digit == 0:
    print("{}{} is {} and is 0".format(st, number, digit))
else:
    print("{}{} is {} and is less than 6 and not 0".format(st, number, digit))
