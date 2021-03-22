# General Data Structures in Python
"""
- Primitives data types: Strings, Lists, Tuples, Dictionary
- Others: Queue, Stack, Graph, Linked List,
"""

import random
# List Comprehensions
under_10 = [x for x in range(10)]
print(str(under_10))
# Get Odd numbers using list comprehension
odds = [x for x in under_10 if x%2 == 1]
print("Odd Numbers in that range are: " + str(odds))

# Get all numbers from a string
s = "asjdf 3 sdjkl6 6 ajksdh 8"
numbers = [x for x in s if x.isnumeric()]
print('numbers ' + ''.join(numbers))

# Get a list of index of a list item
names = ['Peter', 'Pedro', 'Anne', 'Ray']
index = [k for k, v in enumerate(names) if v == 'Anne']
print('index:' + str(index[0]))

# Shuffle
random.shuffle(names)

# 2D list
a =[[1,2], [3,4]]
new_list = [x for b in a for x in b]
print(new_list)


# Other data types
"""
- Stacks: LIFO
- Operations
     - pop()
     - push()
     - peak()
- Python lists are used to create stacks
  - pop() function to remove
  - append() to add a new item on the stack
- A wrapper class can also be used to create a stack
"""

class Stack:
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
    def peak(self):
        if len(self.stack) > 0:
            self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)


"""
- Queue : FIFO
 - Enqueue: adding to the end of the line
 - Dequeue: removing from the first of the line
 
- Queues in python
  - It provides a build in library called deque
"""

from collections import deque

my_queue = deque()
my_queue.append(4)
my_queue.append(9)
print(my_queue)
print(my_queue.popleft())

"""
- MaxHeap: Looks like a tree (Complete binary tree)
 - Every node <=its parent
 - remove Max in O(log n)
 - Easy to implement using a list
- Operations
 - Push()
 - Peek()
 - Pop()
"""
class MaxHeap:
    """
    - Private functions: swap, __floatUp, __bubbleDown, __str
    """
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def peak(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return None

    def pop(self):
        if len(self.heap)>2:
            self.__swap(1, len(self.heap)-1)
            maximum = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            maximum = self.heap.pop()
        else:
            maximum = False
        return maximum

    def remove(self, d):
