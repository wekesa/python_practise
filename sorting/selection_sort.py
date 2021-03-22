"""
- This algorithm segments the list into two parts. sorted and unsorted.
We continuously remove the smallest element of the unsorted segment of the list and append
to the sorted segment.

"""
def selection_sort(nums):
    for i in range(nums):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i

        # This second loop will iterate over the unsorted list
        for j in range(i+1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j

        # Swap the value of the lowest unsorted element with first unsorted
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

    return nums

# Verify it works
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)

