# Optimised Approach
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0

    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        # Update the minimum price if the current price is lower
        if prices[i] < min_price:
            min_price = prices[i]
        # Calculate profit if we sell at the current price
        profit = prices[i] - min_price
        # Update maximum profit if the current profit is greater
        if profit > max_profit:
            max_profit = profit

    return max_profit

# Stock Buy and Sell Problem
# This function calculates the maximum profit that can be made by buying and selling a stock once.
# Time Complexity: O(n) where n is the number of days (length of prices array).
# Space Complexity: O(1) since we are using a constant amount of space.

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    maxPro = maxProfit(prices)
    print("Max profit is: ", maxPro)