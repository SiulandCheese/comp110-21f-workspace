"""An example of a while loop."""

counter: int = 0
maximum: int = int(input("Count up to, but not including what? "))

while counter < maximum: 
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    while (counter + 4) < maximum: 
        print("In case you missed it the first time, The square of " + str(counter) + " is " + str(counter_squared))
        counter = counter + 1
    counter = counter + 1
    
print("Done!")
