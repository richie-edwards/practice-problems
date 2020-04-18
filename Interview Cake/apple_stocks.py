# Time: O(n), where n are number of stock prices; Space: O(1)
def get_max_profit(stock_prices):
    """
    We get a list of prices for a stock where the list indices represent stock prices in chronological order.
    Ex. index 0 is start of market, index 1 is the first minute, index n-1 is the price at the last minute
    of the market.
    We need to return the highest possible profit for the day.
    """
    # assuming we are getting a stock price per minute and list has roughly
    # 420 items
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    for i in range(1, len(stock_prices)):
        current_price = stock_prices[i]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)
    return max_profit


# get_max_profit([10, 7, 5, 8, 11, 9])
# get_max_profit([10, 9, 8, 7])
# get_max_profit([3, 6, 4, 8, 5, 12])
