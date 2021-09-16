"""An exercise in remainders and boolean logic."""

__author__ = "730383189"


# Begin your solution here...

number = 0
tarheels = 0

number = int(input())

if(number % 2 == 0):
    tarheels = 1
elif(number % 7 == 0):
    tarheels = 2
if (number % 2 == 0):
    if(number % 7 == 0):
        tarheels = 3

if(tarheels == 1):
    print("TAR")
elif(tarheels == 2):
    print("HEELS")
elif(tarheels == 3):
    print("TAR HEELS")
elif(tarheels == 0):
    print("CAROLINA")
