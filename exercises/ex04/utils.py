"""List utility functions."""

__author__ = "730383189"


def all(xs: list[int], ys: int) -> bool: 
    i: int = 0
    true_cases: int = 0
    while i < len(xs): 
        if xs[i] == ys: 
            true_cases += 1
            i += 1
        else: 
            i += 1
            break
    return true_cases == i


xs = [2, 2, 2] 
ys = 2

print(all(xs, ys))


def is_equal(a: list[int], b: list[int]) -> bool: 
    i2 = 0 
    j = 0 
    k = 0 
    while j < len(b): 
        while i2 < len(a): 
            if a[i2] == b[j]: 
                i2 += 1
                k += 1
            else: 
                i2 += 1
        j += 1
    return i2 == k 


a = [1, 1, 2]
b = [1, 1]

print(is_equal(a, b))


def max(c: list[int]) -> int: 
    m = 0 
    n = 0 
    while m < len(c): 
        if c[m] > c[0] - 1: 
            n = c[m]
            m += 1
        else: 
            m += 1
    if len(c) == 0: 
        raise ValueError("max() arg is an empty List")
    return n 


c = [100, 10000, 102931]
print(max(c))