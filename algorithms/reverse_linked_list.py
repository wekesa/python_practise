"""
Given a pointer to the head node of a linked list, the task is to reverse the linked list.
We need to reverse the list by changing the links between the nodes

- Examples:
     input:  1->2->3->4-> null
     output: 4->3->2->1-> null

     input: null
     output: null

Iterative Method:
1. Initialize three pointers prev as null, curr as head and next as NULL.
2. Iterate through the linked list. In loop,
3.

Before changing next of current store next node
-    next = curr->next
- Now change next of current
- This is where actual reversing happens
   - curr->next = prev
- Move prev and curr one step forward
prev = curr
curr = next
-
- Time complexity: O(n)
- Space complexity: O(n)
"""

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head


    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Insert new node at the beginning
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node


