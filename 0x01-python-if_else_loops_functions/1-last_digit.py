#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = abs(number) % 10
if number < 0:
    value = -value
if value > 5:
    print(f"Last value of {number:d} is {value:d} and is greater than 5")
elif value == 0:
    print(f"Last value of {number:d} is {value:d} and is 0")
elif value < 6:
    print(f"Last value of {number:d} is {value:d} and is\
 less than 6 and not 0")

