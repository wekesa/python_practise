"""
- A min Heap is complete binary tree which the value in each node is smaller than or equal to the values in the children
- of that node
- Mapping elements of a heap to an array is trivial: If a node is stored at index k, then its left child is stored at index
- 2k + 1 and its right child at index 2k + 2

- Example of a Min Heap
         5                            13
        /  \                         /  \
       10   15                      16     31
      /                             /  \
    30

- Representation of a min heap
- A min heap is a complete binary tree.It is typically represented by an array. The root element will be at Arr[0].
For any ith node, i.e Arr[i]
 - Arr[(i-1)/2] parent node
 - Arr[(2 * i) + 1] returns its left child
 - Arr[(2 * i) + 2] returns its right child

 Operations
 - getMin(): It returns the root element of the minHeap
 - extraMin(): Removes the minimum element from the heap
 - insert(): Inserting a new key takes O(Log n) time. We need to add the key at the end of the tree.

"""
import sys

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * self.maxsize
        self.FRONT = 1

    # Function to return the position of parent for node currently at pos
    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return pos * 2

    def right_child(self, pos):
        return pos * 2 + 1



