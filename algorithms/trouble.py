"""
Given an array of integers (x), and a target (t), you must find out if any two consecutive numbers in the array sum to t. If so, remove the second number.

Example:

x = [1, 2, 3, 4, 5]
t = 3

1+2 = t, so remove 2. No other pairs = t, so rest of array remains:

[1, 3, 4, 5]

Work through the array from left to right.

"""

def trouble(x, t):
    n = len(x)
    if not check_existence(x, t):
        return x
    for i in range(1, n):
        if(x[i-1] + x[i] == t):
            del x[i]
            break
    trouble(x, t)
    return x

def check_existence(x, t):
    n = len(x)
    for i in range(1, n):
        if(x[i-1] + x[i] == t):
            return True
    return False

def trouble(x, t):
    i = 0
    while i < len(x) - 1:
       if x[i] + x[i+1] == t:
           del x[i+1]
       else:
           i += 1
    return x


def sum_parts(l):
    # create a list
    sum_list = []
    # Sum