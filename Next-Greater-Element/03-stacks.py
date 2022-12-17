def nextGreaterElements(nums):
    # store the length of the array
    n = len(nums)

    # initialize the result array with -1 for each element
    result = [-1] * n

    # initialize an empty stack
    stack = []

    # iterate through the array
    for i in range(n):
        # while there are elements in the stack and the current element is greater than the top element of the stack
        while stack and nums[i] > nums[stack[-1]]:
            # set the result of the top element of the stack to the current element
            result[stack.pop()] = nums[i]

        # push the current element onto the stack
        stack.append(i)

    # iterate through the array again
    for i in range(n):
        # while there are elements in the stack and the current element is greater than the top element of the stack
        while stack and nums[i] > nums[stack[-1]]:
            # set the result of the top element of the stack to the current element
            result[stack.pop()] = nums[i]

    # return the result array
    return result
"""

The first loop processes the array from left to right and pushes each element onto the stack. The second loop processes the array from left to right again, and sets the result of each element in the stack to the current element if the current element is greater than the element in the stack.

This approach has a time complexity of O(n) and a space complexity of O(n), as it uses a stack to store the elements that have not yet been processed.
"""
