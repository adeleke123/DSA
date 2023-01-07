## Merge Intervals
Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Input Format
First Parameter - matrix intervals of size `m x n`

## Output Format
Return the matrix.

## Example 1:
```
Input:
     4 2
     1 3
     2 6
     8 10
     15 18
Output:
     [[1,6],[8,10],[15,18]]
Explanation:
4 2 represents the size of the matrix. Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```
## Example 2:
```
Input:
    2 2
    1 4
    4 5
Output:
    [[1,5]]
Explanation: 
    2 2 represents the size of the matrix. Intervals [1,4] and [4,5] are considered overlapping.
 ```
## Constraints:
+ 1 <= intervals.length <= 104
+ intervals[i].length == 2
+ 0 <= starti <= endi <= 104
