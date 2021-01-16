"""
DFS Depth First search
- Input -
- Output -
- Steps -

- Edge cases-

- In Order traversal : print left node, then the root node, then the right
- Pre Order traversal : print root node, then the left node, then the right
- Post Order traversal : print left node, then the right node, then the root
"""
import re

sample_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set() # To keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def eliminate_digits(sentence):
    # re.sub('[0-9]+', '', sentence)
    output = ''.join(c for c in sentence if not c.isnumeric)
    result = ''.join(i for i in sentence if not i.isdigit())
    return re.sub(r'\d+', '', sentence)

def remove_digits(sentence):
    new_sentence = []
    j = 0
    while  j < len(sentence)-1:
        if not re.match(r'\d+', sentence[j]):
            new_sentence.append(sentence[j])
        j+=1
    return "".join(i for i in new_sentence)

def simplified_solution(sentence):
    return re.sub(r'\d+', '', sentence)


def max_non_repeating_characters(S):
    """
    - Input : String of characters
    - Output: Max length of non repeating characters
    - Strategy - Loop through the characters
        - Store characters encountered on a map
        -

    :param S: Example 'ABCABCBB' return 3
    :return:
    """
    pass


def longestUniqueSubsttr(string):
    # Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0

    # starting the inital point of window to index 0
    start = 0

    for end in range(len(string)):

        # Checking if we have already seen the element or not
        if string[end] in seen:
            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[string[end]] + 1)

            # Updating the last seen value of the character
        seen[string[end]] = end
        maximum_length = max(maximum_length, end - start + 1)
    return maximum_length


# Drive Code
#dfs(visited, sample_graph, 'A')
sample_sentence = "This 1djhafd djadh34"
print(simplified_solution(sample_sentence))


class TreeNode:
    def __init__(self, data):
        self.left, self.right = None
        self.data = data

class CalculateHeight:
    def __init__(self):
        self.CalculateHeight = 0

    # function to find height of binary tree
    def height(root):
        # base condition when binary tree is empty
        if root is None:
            return 0
        return max(height(root.left), height(root.right)) + 1


def is_height_balanced(root, Calculateheight):
    """
    :param root:
    :param Calculateheight:
    :return:
    """
    left_height = CalculateHeight()
    right_height = CalculateHeight()

    left = is_height_balanced(root.left, left_height)
    right = is_height_balanced(root.right, right_height)

    CalculateHeight.CalculateHeight = max(left_height.CalculateHeight, right_height.CalculateHeight) + 1

    if abs(left_height.CalculateHeight - right_height.CalculateHeight) <= 1: return left and right

    return False


# function to check if tree is height-balanced or not
def isBalanced(root):
    # Base condition
    if root is None:
        return True

    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)

    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and isBalanced(
            root.left) is True and isBalanced(root.right) is True:
        return True

    # if we reach here means tree is not
    # height-balanced tree
    return False


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]


def longest_word(L):
    """
    -L List of words
    """
    map_words = {}
    words_length = []
    for word in L:
        words_length.append(len(word))
        map_words[len(word)] = word
    maximum_l = max(words_length)
    return map_words[maximum_l]

words = ["two", "three", "asjdfjkahsdfk"]

print(longest_word(words))