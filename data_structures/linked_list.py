# Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a
# contiguous location; the elements are linked using pointers.
# Why Linked List?
#  1. The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also,
#     generally, the allocated memory is equal to the upper limit irrespective of the usage.
#  2. Inserting a new element in an array of elements is expensive because the room has to be created for the
#     new elements and to create room existing elements have to be shifted.
# Advantages over arrays
# 1) Dynamic size
# 2) Ease of insertion/deletion

# A linked list is represented by a pointer to the first node of the linked list. The first node is called the head.
# If the linked list is empty, then the value of the head is NULL.
# Each node in a list consists of at least two parts:
# 1) data
# 2) Pointer (Or Reference) to the next node


# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second = Node(2)
    linked_list.head.next = second
    third = Node(3)
    second.next = third

    linked_list.print_list()
