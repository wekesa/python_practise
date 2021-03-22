"""
- Lowest common ancestor
- Given two values n1 and n2 of a binary search tree, find lowest common ancestor.
- Assumptions
  - Both values exists
             20
            /  \
           8    22
          /  \
        4     12
             /   \
            10    14 w w
"""

# A recursive solution to find LCA of 2 nodes n1 and n2

# A binary tree Node
class Node:
    # Constructor to create a node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find LCA of n1 and n2. The function assumes that both nodes are present
def lca(root, n1, n2):
    # Base case
    if root is None:
        return None

    # if both n1 and n2 are smaller than the root, then the LCA lies on the left
    if(n1 < root.data and n2 < root.data):
        return lca(root.left, n1, n2)

    # If n1 and n2 are greater than the root, the the LCA lies on the right subtree
    if (n1 > root.data and n2 > root.data):
        return lca(root.right, n1, n2)

    return root


# Let us construct the BST shown in the figure
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10
n2 = 14
t = lca(root, n1, n2)
print ("LCA of %d and %d is %d" % (n1, n2, t.data))



# Iterative solution
def lca_iterative(root, n1, n2):
    while root:
        # if both n1 and n2 are smaller than the root then LCA lies on the left
        if root.data > n1 and root.data > n2:
            root = root.left
        # If both n1 and n2 are greater than the root then the LCA lies on the right
        elif root.data < n1 and root.data < n2:
            root = root.right

        else:
            break
    return root




