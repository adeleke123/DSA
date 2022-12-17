def solve(nums):
    # Step 1
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i < 0:
        # Step 2
        nums.reverse()
        return nums

    # Step 3
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1
    replacement = nums[j]

    # Step 4
    nums[i], nums[j] = nums[j], nums[i]

    # Step 5
    nums[i + 1:] = reversed(nums[i + 1:])

    return nums
"""
To find the next permutation, we can follow these steps:

+ Starting from the rightmost element, find the first element that is smaller than its next element. Let's call this element the pivot.

+ If no such element is found, that means the given permutation is already the lexicographically largest permutation. In this case, we can simply reverse the array to get the lexicographically smallest permutation, which is the required next permutation.

+ If a pivot is found, find the smallest element on its right that is greater than the pivot. This is the replacement element.

+ Swap the pivot and the replacement element.

+ Reverse the subarray to the right of the pivot.


"""
