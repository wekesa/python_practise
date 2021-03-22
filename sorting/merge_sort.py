"""
Merge Sort
- This is a divide and conquer algorithm that splits a list in half, keeps splitting the list by 2 until it only
has singular elements.
- Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with other pairs as well
- This process continues until all elements of the unsorted input list.

Explanation.
- We recursively split the list in half until we have lists with size one. We then merge each half that was split,
sorting them in the process.
- Sorting is done by comparing the smallest element of each half.
"""

# Helper method to merge our results
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the lengths so often so lets create variables for them
    left_list_length = len(left_list)
    right_list_length = len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # if the list is a single element we return it
    if len(nums) <= 1:
        return nums
    # Use floor division to get the midpoint, indices must be integers
    mid = len(nums)// 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


def merge_sorted_arrays(nums1, nums2, m, n):
    # Get the last index of num 1
    last = m + n -1
    # Merge in reverse order
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m]
            m -=1
        else:
            nums1[last] = nums2[n]
            n-=1
        last -= 1
    # fill nums 1 from the left over
    while n > 0:
        nums1[last] = nums2[n-1]
        n, last = n-1, last -1
    return nums1
