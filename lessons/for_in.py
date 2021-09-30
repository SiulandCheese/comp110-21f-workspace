"""An example of for in syntax."""

names: list[str] = ["Luis, Sigma, Sarge, Sheriff"]

# Example of iterating through names using while 
print("While Output:")
i: int = 0 
while i < len(names): 
    name: str = names[i]
    print(name) 
    i += 1

# The following for...in loop is the same as the while loop above
print("for...in output:") 
for name in names: 
    print(name) 