"""
Problem
- You have a bunch of coins
- You have an amount of change you need to make
- Do so in a few pieces as you can
Input: A bunch of coins an array of coin denomination and a value
- Example: [5, 10, 50] value: 100
Output: Number of few pieces of coins - 2
-
Approach (Assumptions and possible algorithm):
- Greedy Algorithm - Look for optimal solution
- Recursive solution
"""
def return_change(to_return, coins):
    flag = None
    for c in coins:
        if c == to_return: return c
        if c < to_return:
            flag = c
    temp_balance = round(to_return-flag, 2)
    return [flag] + [return_change(temp_balance, coins)]

def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item


value = 4.33
coins = [0.01, 0.05, 0.10, 0.25, 1.0, 5.0]
print(return_change(value, coins))