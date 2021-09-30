"""List utility functions."""

__author__ = "730383189"


def all(xs: list[int], ys: int) -> bool: 
    """Helps to find if all items are equal to an integer."""
    i: int = 0
    true_cases: int = 0
    while i < len(xs): 
        if xs[i] == ys: 
            true_cases += 1
            i += 1
        else: 
            i += 1
            break
    return true_cases == i and len(xs) > 0


xs: list[int] = [] 
ys = 2

print(all(xs, ys))


# def is_equal(a: list[int], b: list[int]) -> bool: 
#     """Helps to find if all items in two strings are equal."""
#     i = 0 
#     j = 0 
#     k = 0 
#     while j < len(b): 
#         while i < len(a): 
#             if a[i] == b[j]: 
#                 i += 1
#                 k += 1
#             else: 
#                 break
#         j += 1
#         i = 0 
#     return len(a) * len(b) == k 

def is_equal(a: list[int], b: list[int]) -> bool: 
    """Helps to find if all items in two strings are equal."""
    i = 0 
    j = 0
    if len(a) > len(b): 
        while i < len(b): 
            if a[i] == b[i]: 
                j += 1
                i += 1
            else: 
                break 
        return len(a) == j
    elif len(b) > len(a): 
        while i < len(a): 
            if a[i] == b[i]: 
                j += 1
                i += 1
            else: 
                break 
        return len(b) == j 
    elif len(a) == len(b): 
        while i < len(a): 
            if a[i] == b[i]: 
                j += 1
                i += 1
            else: 
                break 
        return len(a) == j 


a = [1, 2, 3]
b = [2, 3]

print(is_equal(a, b))


def max(c: list[int]) -> int: 
    """Helps to find largest number in a string."""
    m = 0 
    n = 0 
    o = 0 
    while m < len(c): 
        while n < len(c): 
            if c[m] >= c[n]: 
                n += 1 
                if n == len(c):
                    o = c[m] 
                    break  
            else: 
                n = 0 
                break 
        m += 1
    if len(c) == 0: 
        raise ValueError("max() arg is an empty List")
    return o 


c = [1, 2, 3, 4, 5]
print(max(c))