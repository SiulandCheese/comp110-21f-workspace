"""Drawing forests in a loop."""

__author__ = "730383189"

TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i = 0

while i < depth:
    print(TREE * (i + 1))
    i = i + 1
