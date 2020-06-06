# Given a string str and an integer K, the task is to find the K-th most frequent character in the string.
# If there are multiple characters that can account as K-th most frequent character then, print any one of them.

from collections import Counter


def kth_character(str_test, k):
    no_of_c = len(str_test)
    count = [0] * 256

    for i in range(no_of_c):
        count[ord(str_test[i])] += 1

    for i in range(256):
        if count[i] == k:
            return chr(i)
    return None


def kth_character_counter(chars, k):
    res = Counter(chars)
    return list(res.keys())[list(res.values()).index(k)]


if __name__ == '__main__':
    characters = 'asdfgsdjhakhdsaaaaa'
    print(kth_character_counter(characters, 2))
