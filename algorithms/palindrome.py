"""
Palindrome is a word that is the same if read from forward and backward
For instance anna
input = String
output = Boolean True or False
Function takes in a string
Take the characters put them in an array
Copy the array then reverse it
"""
"""
- Problem: String which is a sentense
- Input: A sentense which is a string
- Output: A sentense without words with certain values
- 
"""


# Function is_palindrome
def is_palindrome(palindrome_string):
    start_index = 0
    end_index = len(palindrome_string)-1
    while start_index < end_index:
        # You can check whether these characters are valid
        while start_index < end_index and not palindrome_string[start_index].isalpha():
            start_index += 1
        while start_index < end_index and not palindrome_string[end_index].isalpha():
            end_index -= 1
        if palindrome_string[start_index].lower() != palindrome_string[end_index].lower():
            return False
        start_index += 1
        end_index -= 1
    return True


def max_binary_gap(n):
    # Convert to binary
    # use the result to max values
    print(format(n, 'b'))
    return len(max(format(n, 'b').split('1')))


def max_gap(x):
    max_gap_length = 0
    current_gap_length = 0
    for i in range(x.bit_length()):
        if x & (1 << i):
            # Set, any gap is over.
            if current_gap_length > max_gap_length:
                max_gap_length = current_gap_length
            current_gap_length = 0
        else:
            # Not set, the gap widens.
            current_gap_length += 1
    # Gap might end at the end.
    if current_gap_length > max_gap_length:
        max_gap_length = current_gap_length
    return max_gap_length


# Test the function
if __name__ == '__main__':
    valid_string = 'aNna!!'
    invalid_string = 'Peter'

    # print(is_palindrome(valid_string))
    # print(is_palindrome(invalid_string))
    print(max_binary_gap(32))
