# Longest word chain from a list of words
from itertools import permutations


words = ['giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat',
         'hedgehog', 'mouse']


def continuous_starting_sequence(words):
    chain = [words[0]]
    for i in range(1, len(words)):
        if not words[i].startswith(words[i - 1][-1]):
            break
        chain.append(words[i])
    return chain


import re


# Function to remove words with digits
def remove_words_with_digits(sentence):
    if sentence == "":
        return sentence
    words_list = sentence.split(" ")
    words_without_digits = []
    for word in words_list:
        if not re.search(r'\d', word):
            words_without_digits.append(word)
    return " ".join(i for i in words_without_digits)


# Driver Code
if __name__ == '__main__':
    best = max((continuous_starting_sequence(seq) for seq in permutations(words)), key=len)
    print(best)
    print(remove_words_with_digits("Kenya premier legue2"))
