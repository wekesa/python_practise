# Recursion / Dynamic programming
# Given a list of integers return number of sets that can add up to total T provided


def recursion(items, total, items_length):
    # Base cases
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif items_length < 0:
        return 0
    elif total < items[items_length]:
        return recursion(items, total, items_length-1)
    else:
        return recursion(items, total-items[items_length-1], items_length-1) + recursion(items, total, items_length-1)


# Test our recursion function
if __name__ == '__main__':
    items = [2, 4, 6, 4, 10]
    total = 16
    print(recursion(items, total, len(items)-1))


# ------------- Hackarank solution --------------------
n = input()
n = int(n)
l = input().split(" ")


def create_list(str_l):
    int_list = []
    for i in range(len(str_l)):
        int_list.append(int(str_l[i]))
    return int_list


def is_valid(values):
    for j in range(len(values)):
        if (values[j] < 0 or values[j] > 100000):
            return False
    return True


if n >= 1 or n <= 100000:
    new_list = create_list(l)
    if is_valid(new_list):
        print(max(new_list))


n = int(input().strip())



# Balanced Parenthesis
# Given an expression in string
def balanced_parenthesis(S):
    """
    - Input: {[]{()}} - Balanced
    - Input: {{{}]]][ - Unbalanced
    :param S:
    :return:
    - Approach - Using stack data structure
    - Each time an open parenthesis is encountered push it in the stack, and when a
      closed parenthesis is encountered, match it with the top of the stack and pop it. I
    - If the stack is empty at the end it implies that its balanced otherwise its unbalanced
    """
    open_list = ["[", "{", "("]
    closed_list = ["]", "}", ")"]
    stack = []

    for i in S:
        if i in open_list:
            stack.append(i)
        elif i in closed_list:
            pos = closed_list.index(i)
            if(len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
                stack.pop()
        else:
            return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

