# Palindrome is a word that is the same if read from forward and backward
# For instance anna
# input = String
# output = Boolean True or False
# Function takes in a string
# Take the characters put them in an array
# Copy the array then reverse it


# Function is_palindrome
def is_palindrome(palindrome_string):
    start_index = 0
    end_index = len(palindrome_string)-1
    while start_index < end_index:
        left_character = palindrome_string[start_index].lower()
        right_character = palindrome_string[end_index].lower()
        # You can check whether these characters are valid
        if left_character != right_character:
            return False
        start_index += 1
        end_index -= 1
    return True


# Test the function
if __name__ == '__main__':
    valid_string = 'anna'
    invalid_string = 'Peter'

    print(is_palindrome(valid_string))
    print(is_palindrome(invalid_string))
