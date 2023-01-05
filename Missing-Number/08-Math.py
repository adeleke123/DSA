def solve(n, arr):
    # CODE HERE
    # def missing_number(n, arr):
    # Calculate the expected sum of the array
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the array
    actual_sum = sum(arr)
    
    # Return the difference between the expected sum and the actual sum
    return expected_sum - actual_sum
