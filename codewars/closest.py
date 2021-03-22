"""
- [103, 123, 4444, 99, 2000]
- Create a dict
  - {0: 15, 1: 12, 2: 23, 3: 15, 4: 29, 5: 8, 6: 16, 7: 4, 8: 21, 9: 13, 10: 14}
- Sort the dict
  - {7: 4, 5: 8, 1: 12, 9: 13, 10: 14, 0: 15, 3: 15, 6: 16, 8: 21, 2: 23, 4: 29}
-
"""
def closest(strng):
    numbers = strng.split(" ")
    print(numbers)
    if len(numbers) <= 1:
        return []
    weight_dict = {}
    for index, number in enumerate(numbers):
        number_weight = calculate_sum(number)
        weight_dict[index] = number_weight
    print(weight_dict)
    sorted_weights = {k: v for k, v in sorted(weight_dict.items(), key=lambda item: item[1])}
    print(sorted_weights)
    result = get_closest_values(sorted_weights)
    # result[2, 4]
    # {0: 4, 1: 6, 2: 16, 3: 18, 4: 2}
    # [4, 0]
    # [2, 4, 2000]
    # [4, 0, 103]
    first_list = [sorted_weights.get(result[0]), result[0], int(numbers[result[0]])]
    second_list = [sorted_weights.get(result[1]), result[1], int(numbers[result[1]])]

    combined_list = [first_list, second_list]

    return combined_list


def get_closest_values(w):
    """
      - { }
      - {0: 4, 1: 6, 2: 16, 3: 18, 4: 2} Initial dictionary (index => key: weight=> value)
     -  {4: 2, 0: 4, 1: 6, 2: 16, 3: 18} Sorted dictionary

      - 1st iteration = diff [2]
        result [4, 0]
      - 2st iteration = diff [2]
      - 3st iteration = diff [2]
      - 4st iteration = diff [2]
    :param w:
    :return:
    """
    diff = 10 ** 20
    result = [0, 0]
    n = len(w)
    keys = list(w)
    values = list(w.values())
    for i in range(n - 1):
        if (values[i + 1] - values[i]) < diff:
            diff = values[i + 1] - values[i]
            result[0] = keys[i]
            result[1] = keys[i + 1]
    print(result)
    return result


def calculate_sum(number):
    weight = 0
    for i in str(number):
        weight += int(i)
    return weight


# Anonymous function

print(closest("103 123 4444 99 2000"))