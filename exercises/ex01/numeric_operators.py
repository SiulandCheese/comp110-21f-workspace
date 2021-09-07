"""Code to take two numbers and showcase some common operations with them."""

__author__ = "730383189"

left_number: str = input("Left-hand side: ")
right_number: str = input("Right-hand side: ")

solution_1: int = int(left_number) ** int(right_number)
solution_2: float = int(left_number) / int(right_number)
solution_3: int = int(left_number) // int(right_number)
solution_4: int = int(left_number) % int(right_number)

print(left_number + " ** " + right_number + " is " + str(solution_1))
print(left_number + " / " + right_number + " is " + str(solution_2))
print(left_number + " // " + right_number + " is " + str(solution_3))
print(left_number + " % " + right_number + " is " + str(solution_4))