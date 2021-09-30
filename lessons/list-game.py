"""Examples of using lists in a simple 'game'."""


from random import randint


rolls: list[int] = list()  

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1: 
    rolls.append(randint(1, 6))

print(rolls)

# Sum the values of our rolls! 
x: int = 0
while len(rolls) != 0: 
    x = rolls[len(rolls) - 1] + x
    rolls.pop()

print(x)