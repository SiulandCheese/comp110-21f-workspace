"""Finding duplicate letters in a word."""

__author__ = "730383189"

given_word: str = input("Enter a Word: ")

i = 0
n = 1
k = 0

while i < len(given_word):
    while n < len(given_word):
        if given_word[i] == given_word[n]:
            print("Found duplicate: True")
            k = k + 1
            break
        else: 
            n = n + 1
    i = i + 1
    n = 1 + i 
    if k == 1: 
        break

if k == 0:
    print("Found duplicate: False")
