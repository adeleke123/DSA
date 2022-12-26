def solve(n, nums, target):
    # CODE HERE
    # def twoSum(n: int, nums: List[int], target: int) -> List[int]:
    # Create a hash table to store the indices of the numbers
    indices = {}
    for i, num in enumerate(nums):
        # Check if target - num is in the hash table
        if target - num in indices:
            # Return the indices of the two numbers
            return [indices[target - num], i]
        # Store the index of the current number in the hash table
        indices[num] = i

