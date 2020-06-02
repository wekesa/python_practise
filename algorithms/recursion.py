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
