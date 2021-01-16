'''
- Given an unsorted array of integers, find the length of the longest continuous increasing subsequence ()
: Example:
Input: [3,4,6,4,7]
Output: 3

Endge case:
-

'''

def find_longest_continuous_subsequence(numbers):
    """
    :param numbers:
    :return:
    """
    if not numbers:
        return 0
    start, result = 0, 1
    for end in range(1, len(numbers)):
        if(numbers[end-1] >= numbers[end]):
            start=end
        result = max(result, end-start+1)
    return result

def character_frequency(str):
    """
    :param str: string to be processed
    :return: a dictionary with length of each char
    """
    characters_dict = {}
    for char in str:
        keys = characters_dict.keys()
        if char in keys:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict

def string_both_ends(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2:]

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1

def character_mix_up(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    return new_str1 + " " + new_str2


def binary_search(arr, lower_index, upper_index, value):
    if upper_index < lower_index:
        return None
    else:
       midval = lower_index + ((upper_index-lower_index)/2)
       if arr[midval] > value:
           return binary_search(arr, lower_index, midval-1, value)
       elif arr[midval] < value:
           return binary_search(arr, midval+1, upper_index, value)
       else:
           return midval

'''
- Problem: Reverse a strings
- Input: a string
- Output: a reversed String

- Example: today
  return: yadot
  
  Steps: 
  - 
'''

"""
- Recursive solution for coin change problem
- Input: List of coins available, n- value 
- Output: int x.. all possible ways inwhich we can get the change

Example:
    - Given: N=4, S={1,2,3} retrun 4
"""

def count_coins(S, m, n):
    """
    @desc Recursive function to get coins
    :param S:
    :param m:
    :param n:
    :return:
    """
    # Base case
    if n == 0:
        return 1

    if n < 0:
        return 0

    if m<=0 and n >= 1:
        return 0

    # count is sum of solutions (i)
    return count(S, m - 1, n) + count(S, m, n - S[m - 1]);


# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):
    # We need n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    table = [[0 for x in range(m)] for x in range(n + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, n + 1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[n][m - 1]


# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
print(count(arr, m, n))


# m is size of coins array (number of different coins)
def minCoins(coins, m, V):
    # base case
    if (V == 0):
        return 0

    # Initialize result
    res = sys.maxsize

    # Try every coin that has smaller value than V
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V - coins[i])

            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1

    return res