"""
- Problem : Given a string check if its a palindrome

Example 1
input: anna
output: true

Example 2
input: Peter
output: false


Possible Approach
- Reverse the string
- Compare the reversed string with the original string
- If matches return true otherwise return false
"""

def is_palindrome(S):
    """
    @desc takes a string as input and return True or False if its palindrome
    :param S:
    :return: bool
    """
    start_index = 0
    end_index = len(S) - 1
    while start_index < end_index:
        if (S[start_index] != S[end_index]):
            return False
        start_index +=1
        end_index -=1
    return True

    # reversed_string = reversed(S)
    # return list(S) == list(reversed_string)


print(is_palindrome("aoonna"))




"""
- Problem: 

- Input:
- Output: 

Example:
- 
- 

Example: 
- 
- 
"""

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right= TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


class Solution:
    def is_validBST(self, root):
        return self.solve(root, -1000000, 10000000)
    def solve(self, root, min_value, max_value):
        if root == None or root.data == 0:
            return True
        if root.data <= min_value or root.data>= max_value:
            return False
        return self.solve(root.left, min_value, root.data) and self.solve(root.right, root.data, max_value)



def create_min_heap():
    """
    Creation of a min heap
    Operations that can be performed
    - Insert - A new element is always inserted into the highest and then the left most position that is available.
    - Delete - Remove any element, take it out of the tree and replace it with the lowest then right most element in the tree
    -
    :return:
    """