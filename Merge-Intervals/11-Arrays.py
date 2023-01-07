def solve(intervals):
    # CODE HERE
    # Sort the intervals by their starting times
    intervals.sort(key=lambda x: x[0])

    # Initialize the merged list and the current interval
    merged = []
    current_interval = intervals[0]

    # Iterate through the rest of the intervals
    for interval in intervals[1:]:
        # If the current interval overlaps with the next interval,
        # merge the two intervals into a single interval
        if interval[0] <= current_interval[1]:
            current_interval = [min(current_interval[0], interval[0]),
                               max(current_interval[1], interval[1])]
        # If the current interval does not overlap with the next interval,
        # add the current interval to the merged list and update the current interval
        else:
            merged.append(current_interval)
            current_interval = interval

    # Add the final interval to the merged list
    merged.append(current_interval)

    return merged

"""
This program is trying to merge a list of overlapping intervals into a list of non-overlapping intervals.

The function solve takes a single argument:

intervals is a list of intervals, where each interval is a list containing a start time and an end time.
The function starts by sorting the intervals by their starting times. This is done using the sort method and a key function that returns the starting time of each interval.

Next, the function initializes an empty list called merged to store the merged intervals, and a variable current_interval to the first interval in the sorted list.

Then, the function iterates through the rest of the intervals in the sorted list. For each interval interval, the function does the following:

If interval does not overlap with current_interval (that is, if the start time of interval is later than the end time of current_interval), the function adds current_interval to the merged list and sets current_interval to interval.

If interval does overlap with current_interval, the function merges the two intervals into a single interval by taking the minimum of the start times and the maximum of the end times, and updates current_interval with this merged interval.

After the loop has finished, the function adds current_interval to the merged list. Finally, the function returns the merged list.

Here's an example of how the function might be used:

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = solve(intervals)
print(result)  # prints [[1, 6], [8, 10], [15, 18]]

intervals = [[1, 4], [4, 5]]
result = solve(intervals)
print(result)  # prints [[1, 5]]

""""
