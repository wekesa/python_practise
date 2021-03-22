"""
- HEAP SORT
- This is a popular sorting algorithm
- Like Insertion and selection sorts, it also segments the list into sorted and unsorted parts.
- It converts the the unsorted segment of the list to a Heap data structure, so that we can efficiently
determine the largest element.
- The first step transforming it to a MAX HEAP. A binary tree where the biggest element is the root element
- We then rebuild our max heap which now has less value, placing the largest value before the last item of the list
- We iterate this process of building the heap until all nodes are removed.
-
-
- Implementation
- We create a helper function called heapify to implement this algorithm
"""

def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # if the left child of the root is a valid index and the element is greater than the current largest element
    # then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Similarly we do the same for the right child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    # Create a max heap from a list
    # The second argument indicates that we stop at the element before -1, i.e the first element of the list
    # The 3rd argument indicates we iterate backwards, reducing the the count by i 1.

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the root element to the end of the list
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


# Verify it works
random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)