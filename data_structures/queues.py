# Queue is a linear data structure that stores items in First In First Out (FIFO) manner.
# With a queue the least recently added item is removed first.
# A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.
# Operations associated with queue are:
#    - Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition –
#      Time Complexity : O(1)
#    - Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed.
#      If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
#    - Front: Get the front item from queue – Time Complexity : O(1)
#    - Rear: Get the last item from queue – Time Complexity : O(1)
# Queue in Python can be implemented by the following ways:
#    - list
#    - collections.deque
#    - queue.Queue

from collections import deque
from queue import Queue


def queue_using_list():
    queue = []
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print(queue)
    # remove item
    queue.pop(0)
    print(queue)


def queue_using_deque():
    queue = deque()
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print(queue)

    # remove an item
    queue.popleft()

    print(queue)


def queue_using_queue_module():
    queue = Queue(maxsize=3)
    queue.put('a')
    queue.put('b')
    queue.put('c')
    print(queue)
    # Remove an item
    queue.get()
    queue.get()
    print(queue)


if __name__ == '__main__':
    queue_using_list()
    queue_using_deque()
    queue_using_queue_module()


# A queue is a data structure that operates in a first in first out manner (FIFO)
# Operations
# - Enqueue
# - Dequeue
# - IsFull
# - Peek
# - IsEmpty

# Queue Operations
# - FRONT
# - REAR

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)


