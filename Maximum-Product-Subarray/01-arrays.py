def solve(n, arr):
    # CODE HERE
    if not arr:
        return 0

    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > 0:
            max_product = max(max_product * arr[i], arr[i])
            min_product = min(min_product * arr[i], arr[i])
        else:
            max_product, min_product = max(min_product * arr[i], arr[i]), min(max_product * arr[i], arr[i])

        result = max(result, max_product)

    return result

"""
To find the contiguous subarray with the largest product, you can use a single pass through the array, keeping track of the maximum and minimum product seen so far.

Here is some pseudocode that demonstrates how this can be done:

max_product = arr[0]
min_product = arr[0]
result = arr[0]
for i = 1 to length(arr) - 1:
    # update max_product and min_product
    if arr[i] > 0:
        max_product = max(max_product * arr[i], arr[i])
        min_product = min(min_product * arr[i], arr[i])
    else:
        max_product = max(min_product * arr[i], arr[i])
        min_product = min(max_product * arr[i], arr[i])

    # update result
    result = max(result, max_product)

return result

"""
