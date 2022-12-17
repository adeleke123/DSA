## Next Greater Element

Given a circular integer array `nums` (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in `nums`.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn’t exist, return -1 for this number.

## Input Format

First Parameter - number `n`

Second Parameter - array nums of size n

## Output Format

Return the array

## Example 1:
```
Input:
    4
    1 3 2 4
Output:
    3 4 4 -1
Explanation:
    In the array, the next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4 needs to search circularly. Since there exists no next number greater than 4, it's -1.
```
## Example 2:
```
Input:
    5
    6 8 0 1 3
Output:
    8 -1 1 3 6
Explanation:
    In the array, the next larger element to 6 is 8, 8 is -1, 0 is 1, 1 is 3 and 3 is 6.
```
## Constraints:
+ 1 ≤ n ≤ 104
+ -109 ≤ arr[i] ≤ 109
+ Expected Time Complexity: O(N)
+ Expected Auxilliary Space: O(N)
