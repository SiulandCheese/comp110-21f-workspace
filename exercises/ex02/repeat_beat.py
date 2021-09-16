"""Repeating a beat in a loop."""

__author__ = "730383189"

beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
beat_string: str = ("")

i = 0

if i < times: 
    while i < times: 
        beat_string = beat_string + " " + beat 
        i = i + 1
    print(beat_string)
else: 
    print("No beat...")