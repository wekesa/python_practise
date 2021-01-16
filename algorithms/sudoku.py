""""
- Sudoku check if its valid with partially filled cells
- Algorithm>
    - Check if the rows and columns contain value 1-9 without repetition
    - If any of the row or column violates this.. then return its invalid
    - Check if subsquares contain values 1-9 without repeating..
"""


# 1. Check if the rows and columns contain values 1-9, without repetition.
# 2. If any row or column violates this condition, the Sudoku board is invalid.
# 3. Check to see if each of the 9 sub-squares contains values 1-9, without repetition.
#    If they do, the Sudoku board is valid; otherwise, it is invalid.

# Function to check if a given row is valid. It will return:
# -1 if the row contains an invalid value
# 0 if the row contains repeated values
# 1 is the row is valid.

def valid_row(row, grid):
    temp = grid[row]
    # temp = list(filter(lambda a: a != 0, temp))
    temp = [a for a in temp if a !=0 ]
    if any(i < 0 and i < 9 for i in temp):
        print("Invalid values")
        return -1
    elif(len(temp) != len(set(temp))):
        return 0
    else:
        return 1
# Function to check if a column is valid
# -1 if column contains an invalid value
# 0 if the column contains repeated values
# 1 if the column is valid
def valid_column(column, grid):
    # Extract the column
    col = [row[column] for row in grid]
    col = list(filter(lambda i : i != 0, col))
    if any(i < 0 and i < 9 for i in col):
        return -1
    elif(len(col) != len(set(col))):
        return 0
    else:
        return 1
# Function to check if all the subsquares are valid. it will return
# -1 if the subsquare contains an invalid value
# 0 if the subsquare contains repeated value
# 1 if the subsquare are valid
def valid_sub_grid(grid):
    for row in range(0,9,3):
        for col in range(0,9,3):
            temp = []
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if grid[r][c] != 0:
                        temp.append(grid[r][c])
            if any(i < 0 and i > 9 for i in temp):
                return -1
            elif len(temp) != len(set(temp)):
                return 0
    return 1



def valid_row(row, grid):
    temp = grid[row]
    # Removing 0's.
    temp = list(filter(lambda a: a != 0, temp))
    # Checking for invalid values.
    if any(i < 0 and i > 9 for i in temp):
        print("Invalid value")
        return -1
    # Checking for repeated values.
    elif len(temp) != len(set(temp)):
        return 0
    else:
        return 1


# Function to check if a given column is valid. It will return:
# -1 if the column contains an invalid value
# 0 if the columncontains repeated values
# 1 is the column is valid.
def valid_col(col, grid):
    # Extracting the column.
    temp = [row[col] for row in grid]
    # Removing 0's.
    temp = list(filter(lambda a: a != 0, temp))
    # Checking for invalid values.
    if any(i < 0 and i > 9 for i in temp):
        print("Invalid value")
        return -1
    # Checking for repeated values.
    elif len(temp) != len(set(temp)):
        return 0
    else:
        return 1


# Function to check if all the subsquares are valid. It will return:
# -1 if a subsquare contains an invalid value
# 0 if a subsquare contains repeated values
# 1 if the subsquares are valid.
def valid_subsquares(grid):
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            temp = []
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if grid[r][c] != 0:
                        temp.append(grid[r][c])
            # Checking for invalid values.
            if any(i < 0 and i > 9 for i in temp):
                print("Invalid value")
                return -1
            # Checking for repeated values.
            elif len(temp) != len(set(temp)):
                return 0
    return 1


# Function to check if the board invalid.
def valid_board(grid):
    # Check each row and column.
    for i in range(9):
        res1 = valid_row(i, grid)
        res2 = valid_col(i, grid)
        # If a row or column is invalid then the board is invalid.
        if (res1 < 1 or res2 < 1):
            print("The board is invalid")
            return
    # If the rows and columns are valid then check the subsquares.
    res3 = valid_subsquares(grid)
    if (res3 < 1):
        print("The board is invalid")
    else:
        print("The board is valid")


def print_board(grid):
    for row in grid:
        print(row)


board = [[1, 4, 7, 0, 0, 0, 0, 0, 3],
         [2, 5, 0, 0, 0, 1, 0, 0, 0],
         [3, 0, 9, 0, 0, 0, 0, 0, 0],
         [0, 8, 0, 0, 2, 0, 0, 0, 4],
         [0, 0, 0, 4, 1, 0, 0, 2, 0],
         [9, 0, 0, 0, 0, 0, 6, 0, 0],
         [0, 0, 3, 0, 0, 0, 0, 0, 9],
         [4, 0, 0, 0, 0, 2, 0, 0, 0],
         [0, 0, 1, 0, 0, 8, 0, 0, 7]]
print_board(board)
valid_board(board)
board2 = [[1, 4, 4, 0, 0, 0, 0, 0, 3],
          [2, 5, 0, 0, 0, 1, 0, 0, 0],
          [3, 0, 9, 0, 0, 0, 0, 0, 0],
          [0, 8, 0, 0, 2, 0, 0, 0, 4],
          [0, 0, 0, 4, 1, 0, 0, 2, 0],
          [9, 0, 0, 0, 0, 0, 6, 0, 0],
          [0, 0, 3, 0, 0, 0, 0, 0, 9],
          [4, 0, 0, 0, 0, 2, 0, 0, 0],
          [0, 0, 1, 0, 0, 8, 0, 0, 7]]
print_board(board2)


# maximum sum of a subarray of size k

def maxSum(arr, n, k):
    # n must be greater than k
    if not n > k:
        print("Invalid")
        return -1

    # Compute sum of first window of size k
    max_sum = 0
    window_sum = sum(arr[:k])

    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum


# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))


# Maximum length word formed

def max_length(list_strings):
    """
    - Generate all possible combination then
     - check if they are unique
     - Keep track of length of unique strings formed
    :param list_strings:
    :return:
    """

    result = [float('-inf')]

    unique_char("", arr, 0, result)

    if not result[0] == float('-inf'):
        return result[0]
    return 0


def unique_char(cur, arr, index, result):
    # End of the array
    if index == len(arr):
        return

    # Iterating from the current word to the end of the array
    for index in range(index, len(arr)):

        # If current word + next word have all unique characters
        if len(set(cur + arr[index])) == len(list(cur + arr[index])):
            # Compare the actual lenth with the previous max
            result[0] = max(result[0], len(cur + arr[index]))
            # Make a new call with concatenate words
            unique_char(cur + arr[index], arr, index + 1, result)
