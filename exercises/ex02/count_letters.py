"""Counting letters in a string."""

__author__ = "730383189"


search_letter: str = input("What letter do you want to search for?: ")
given_word: str = input("Enter a word: ")
i = 0
count = 0

while i < len(given_word):
    if search_letter == given_word[i]:
        count = count + 1
    else: 
        0 ** 0
    i = i + 1

print("Count: " + str(count))