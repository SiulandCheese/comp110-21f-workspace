"""A Corrected Program."""

__Author__ = "730383189"

choice: int = int(input("Feed me a number! "))

if choice < 50: 
    if choice < 25:
        print("A")
    else:
        print("B")
else: 
    if choice > 75:
        print("C")
    else: 
        print("D")
