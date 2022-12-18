def maxArea(n, arr):
    left, right = 0, n - 1
    max_area = 0
    
    while left < right:
        current_area = min(arr[left], arr[right]) * (right - left)
        max_area = max(max_area, current_area)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

"""

To solve this problem, you can use a two-pointer approach. Initialize two pointers, left and right, to the beginning and end of the array, respectively. 

Then, while left is less than right, do the following:

Calculate the current area by taking the minimum of arr[left] and arr[right] and multiplying it by the distance between left and right.

Update the maximum area if necessary.

If arr[left] is less than arr[right], increment left. Otherwise, decrement right.

"""
