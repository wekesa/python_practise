"""
- Given a value V, we want to make change for V cents, and we have infinite supply of each of C
= {C1, C2, C3 .... Cm} valued coins, what is the minimum number of coins to make change. If its not possible to make
change print -1



Examples:
    Input: coins = [25, 10, 5], V 30
    output: minimum 2

Approach: Naive recursive solution



"""
import sys
def minCoins(coins, m, V):
    if V == 0:
        return 0
    # Initialize results = sys.maxsize
    res = sys.maxsize
    # Try every coin that has a smaller value thatn V
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V-coins[i])

            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1

# time complexity here is exponential


# A Dynamic Programming based Python3 program to
# find minimum of coins to make a given change V
import sys


# m is size of coins array (number of
# different coins)
def minCoins(coins, m, V):
    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [0 for i in range(V + 1)]

    # Base case (If given value V is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, V + 1):
        table[i] = sys.maxsize

    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, V + 1):

        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[V] == sys.maxsize:
        return -1

    return table[V]


# Driver Code
if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    m = len(coins)
    V = 11
    print("Minimum coins required is ",
          minCoins(coins, m, V))

# This code is contributed by ita_c
