def solve(n, arr):
    # CODE HERE
    nums = arr
    # Create a hash set to store the values
    values = set()
    for num in nums:
        # Check if the current number is in the hash set
        if num in values:
            return 1
        # Add the current number to the hash set
        values.add(num)
    return 0

"""
This program is trying to determine whether there are any duplicate elements in a list of integers.

The function solve takes two arguments:

n is the number of elements in the list.
arr is the list of integers.
Inside the function, the variable nums is defined as a copy of the list arr.

Then, the function creates an empty set called values. A set is a collection of unique elements, so adding an element to a set will not create a duplicate if the element is already in the set.

Next, the function iterates through each element num in the list nums.

For each element, the function checks if the element is already in the set values. If it is, the function returns 1. Otherwise, the function adds the element to the set values.

Finally, after the loop has finished, the function returns 0. This indicates that there were no duplicate elements in the list.

Here's an example of how the function might be used:

n = 4
arr = [1, 2, 3, 4]
result = solve(n, arr)
print(result)  # prints 0

n = 4
arr = [1, 2, 3, 3]
result = solve(n, arr)
print(result)  # prints 1

"""
