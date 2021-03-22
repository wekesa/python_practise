# Python3 program to find the length
# of the longest substring
# without repeating characters
def longestUniqueSubsttr(string):
    # last index of every character
    last_idx = {}
    max_len = 0

    # starting index of current
    # window to calculate max_len
    start_idx = 0

    for i in range(0, len(string)):

        # Find the last index of str[i]
        # Update start_idx (starting index of current window)
        # as maximum of current value of start_idx and last
        # index plus 1
        if string[i] in last_idx:
            start_idx = max(start_idx, last_idx[string[i]] + 1)

        # Update result if we get a larger window
        max_len = max(max_len, i - start_idx + 1)

        # Update last index of current char.
        last_idx[string[i]] = i

    return max_len



def longest_unique_characters(s):
    sub = {}
    current_sub_start = 0
    current_length = 0
    longest = 0

    for i, letter in enumerate(s):
        if letter in sub and sub[letter] >= current_sub_start:
            current_sub_start = sub[letter] + 1
            current_length = i - sub[letter]
            sub[letter] = i

        else:
            sub[letter] = i
            current_length += 1
            if current_length > longest:
                longest = current_length
    return longest