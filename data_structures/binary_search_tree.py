"""
- Given a BST, write an efficient function to delete a given key in it.
- There are 3 possible cases to consider while deleting a node from a BST
 1. Deleting a node without children from a tree.
    e.g deleting 18 on this tree below
                  15
                 /   \
                10    20
                / \   / \
               8   12 18  25


 2. Deleting a node with 2 children lets say node N. Do not delete N. Instead, choose either its inorder successor or
    inorder predecessor node R. Copy the value of R to N, then recursively call delete on R until reaching one of the first
    2 cases.
 3. Deleting a node with one child: remove node and replace it with its children
Broadly speaking, nodes with children are harder to delete. As with all binary trees, a node's inorder successor is its
right subtree left most child, and a nodes inorder predecessor is its left subtree's rightmost child. In either case,
this node will have zero or one child. Delete it according to one of the 2 simpler cases
"""

# A class to store BST node

class Node:
    # constructor to store data and pointers to left and right node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

# Function to perform inorder traversal on a BST
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

# Helper function to find minimum value node in the subtree rooted at curr
def get_minimum(curr):
    while curr.left:
        curr = curr.left
    return curr

# Recursive function to insert a key into a BST
def insert(root, key):
    # If the root is none create an node and return it
    if root is None:
        return Node(key)
    # if key is less than the root recur for the left subtree
    if root.data > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


# Function to delete a node on a BST
def delete_node(root, key):
    # Pointer to store the parent of the current node
    parent = None
    # start with root node
    curr = root
    # search the key and set its parent pointer
    while curr in curr.data != key:
        # update the parent to the current node
        parent = curr
        # if a given key is less than the current node, go to the left subtree otherwise go to the left subtree
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    # return none if key is not found in the tree
    if curr is None:
        return root

    # Case 1: Node to be deleted has no children
    if curr.left is None and curr.right is None:
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        else:
            root = None

    # Case 2: node to be deleted has 2 children
    elif curr.left and curr.right:
        # Find its onorder successor node
        successor = get_minimum(curr.right)
        # store successor value
        val = successor.data
        # Recursively delete the successor.
        delete_node(root, successor.data)
        curr.data = val

    # Case 3: node to be deleted has only one child
    else:
        if curr.left:
            child = curr.left
        else:
            child = curr.right
        # if node to be deleted is not a root node, set its parent to its child
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            root = child

    return root


if __name__ == '__main__':

    keys = [15, 10, 20, 8, 12, 16]

    root = None
    for key in keys:
        root = insert(root, key)

    root = deleteNode(root, 16)
    inorder(root)
