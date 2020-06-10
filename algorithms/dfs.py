# Problem solving skills
# Understanding the problem
# Design
# algorithms and data structure
# reversing a string without inbuilt methods
#
#
#
# Algorithm
# Inputs - string (Characters)
# Output - reversed string (Reversed characters)
# start
# var input_string
# var output_string
# for i in input_string:
#
#
#


def reverse_string(input_string):
    index = len(input_string)
    reversed_string = []
    while index > 0:
        reversed_string += input_string[index - 1]
        index -= 1
    print(reversed_string)


if __name__ == '__main__':
    example_string = "ajdhjfabjdakdjfh"
    reverse_string(example_string)


