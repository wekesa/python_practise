# A stack is a linear data structure that stores items in a Last-In/ First-Out (LIFO) or
#    First-In /Last-Out (FIFO) manner.
# - The insert and delete operations are often called push and pop
# - Functions associated with stack are
#   1. empty() - returns whether stack is empty - Time complexity: O(1)
#   2. size() - Returns the size of the stack - Time Complexity: O(1)
#   3. top() - Returns a reference to the top most element of the stack - Time complexity: O(1)
#   4. push(g) - Deletes an element from the top of the stack. - Time complexity: O(1)
#
#   ways to implement in Python: Using python libraries
#   - List
#   - collections.deque
#   - queue.LifoQueue
print("Before import")
from collections import deque
from queue import LifoQueue


def stack_using_list():
    stack = []
    stack.append('itemOne')
    stack.append('itemTwo')
    stack.append('itemThree')

    print(stack)
    print(stack.pop())
    print(stack)


def stack_using_deque():
    stack = deque()
    stack.append('a')
    stack.append('b')
    stack.append('c')
    print(stack)
    print(stack.pop())
    print(stack)

def stack_using_queue_module():
    stack = LifoQueue(maxsize=3)
    print(stack.qsize())
    stack.put('a')
    stack.put('b')
    stack.put('c')

    print(stack.full())
    print(stack.qsize())
    print(stack.get())

print('Before __name__ guard')
if __name__ == '__main__':
    stack_using_list()
    stack_using_queue_module()
print('After name guard')


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

        # Use list pop method to remove element

    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()
