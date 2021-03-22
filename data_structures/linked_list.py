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


"""
- A linked list is a sequence of data elements which are connected via links. Each data element contains a connection to 
another data element in form of a pointer. Python does not have linked lists in its standard library. 
- I will implement it using the concept of nodes. Implement a node class 
- Singly linked lists.. In this type of data structure these is only one link between any two data elements.
- 

- Creating a linked list 
"""

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def insert_begging(self, newdata):
        new_node = Node(newdata)
        new_node.nextval = self.headval
        self.headval = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.headval is None:
            self.headval = new_node
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = new_node



list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3



# Merge two sorted lists
class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def merge_list(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next