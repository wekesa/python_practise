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


if __name__ == '__main__':
    best = max((continuous_starting_sequence(seq) for seq in permutations(words)), key=len)
    print(best)
