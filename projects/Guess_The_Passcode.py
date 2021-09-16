"""A Game That Makes You Guess A Passcode."""

import random

print("Hello there! I hope you're ready to try and guess my passcode. It is three digits long, have fun!")

Password_Digit_1: int = random.randint(0, 9)
Password_Digit_2: int = random.randint(0, 9)
Password_Digit_3: int = random.randint(0, 9)

Password: str = str(Password_Digit_1) + str(Password_Digit_2) + str(Password_Digit_3)

Password_Guess_1: int = int(input("What do you think the first digit is? "))
Password_Guess_2: int = int(input("What do you think the second digit is? "))
Password_Guess_3: int = int(input("What do you think the final digit is? "))

Password_Guess = str(Password_Guess_1) + str(Password_Guess_2) + str(Password_Guess_3)

while Password != Password_Guess:
    if Password_Digit_1 == Password_Guess_1:
        print("You got the first digit right!")
    else: 
        print("Sorry, doesn't look like you got digit one right.")
        if Password_Digit_1 > Password_Guess_1:
            print("Digit 1 is higher than what you guessed!")
            Passsword_Guess_1 = int(input("Guess digit 1 again! "))
        else: 
            print("Digit 1 is lower than what you gussed!")
            Passsword_Guess_1 = int(input("Guess digit 1 again! "))

    if Password_Digit_2 == Password_Guess_2:
        print("You got the second digit right!")
    else: 
        print("Sorry, doesn't look like you got digit two right.")
        if Password_Digit_2 > Password_Guess_2:
            print("Digit 2 is higher than what you guessed!")
            Passsword_Guess_2 = int(input("Guess digit 2 again! "))
        else: 
            print("Digit 2 is lower than what you gussed!")
            Passsword_Guess_2 = int(input("Guess digit 2 again! "))

    if Password_Digit_3 == Password_Guess_3:
        print("You got the final digit right!")
    else: 
        print("Sorry, doesn't look like you got the last one right.")
        if Password_Digit_3 > Password_Guess_3:
            print("Digit 3 is higher than what you guessed!")
            Passsword_Guess_3 = int(input("Guess digit 3 again! "))
        else: 
            print("Digit 3 is lower than what you gussed!")
            Passsword_Guess_3 = int(input("Guess digit 3 again! "))
    Password_Guess = str(Password_Guess_1) + str(Password_Guess_2) + str(Password_Guess_3)

print("Congrats, you win!")
