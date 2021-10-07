"""List utility functions part 2."""

__author__ = "730383189"

# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    """Prints only the even numbers."""
    i: int = 0 
    b: list[int] = []
    while i < len(a): 
        if a[i] % 2 == 0: 
            b.append(a[i])
    i += 1

    return b


def sub(a: list[int], b: int, c: int) -> list[int]: 
    """Creates one list between two indexes specified."""
    i: int = 0 
    list_2: list[int] = []
    while i < len(a): 
        if i >= b and i < c:
            list_2.append(a[i])
        i += 1 
    
    return list_2


def concat(a: list[int], b: list[int]) -> list[int]: 
    """Merges two lists together"""
    i: int = 0 
    c: list[int] = []
    while i < len(a):
        c.append(a[i])
        i += 1
    
    i = 0 
    while i < len(b): 
        c.append(b[i])
        i += 1
    
    return c