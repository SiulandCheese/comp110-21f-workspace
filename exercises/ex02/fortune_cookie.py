"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730383189"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


random_integer: int = randint(0, 3)

print("Your fortune cookie says...")

if random_integer == 0: 
    print("You will fall in love soon!")
else: 
    if random_integer == 1:
        print("You will become rich soon!")
    else:
        if random_integer == 2:
            print("You will get an A on your next exam!")
        else: 
            print("You will eat a delicious meal in a place you least expect!")

print("Now, go spread positive vibes!")