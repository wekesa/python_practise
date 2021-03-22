"""
- Need to arrange data in order to process it efficiently
- Looking into popular sorting algorithms
- Sorting lists in ascending order
- Adapting them to your needs
-

Bubble sort
- A simple sorting algorithm that iterates over a list, comparing elements in pairs and swapping
then until the larger element bubbles up to the end of the list
- If the first element is larger than the second element we swap them. If they are already in order we leave them
as is. We then move the next pair of elements, compare values and swap as necessary.
"""

def bubble_sort(nums):
    """
    - Worst case scenario the algorithm would swap every element in the array
    - time complexity is O(n^2)
    :param nums:
    :return:
    """
    # We set swapped to True so that the loop looks at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            swapped = True
    return nums

# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)