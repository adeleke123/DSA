def solve(n, prices):
    # CODE HERE
    if not prices:
        return 0

    max_profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - min_price)
    return max_profit

"""
To maximize profit, you need to find the day with the lowest price to buy and the day with the highest price to sell.

One way to do this is to use a single pass through the array, keeping track of the minimum price seen so far and the maximum profit achieved so far.

Here is some pseudocode that demonstrates how this can be done:

max_profit = 0
min_price = prices[0]
for i = 1 to length(prices) - 1:
    if prices[i] < min_price:
        min_price = prices[i]
    else:
        max_profit = max(max_profit, prices[i] - min_price)
return max_profit

This approach has a time complexity of O(n) and a space complexity of O(1), as it only uses a single variable to store the minimum price and another variable to store the maximum profit.

"""
