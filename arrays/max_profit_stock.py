from typing import List


def max_profit_one_transaction(prices: List[int]) -> int:
    """
    Find the maximum profit from a single buy and sell transaction.
    Must buy before selling.
    Time: O(n), Space: O(1)
    
    Args:
        prices: List of stock prices where index is the day
    Returns:
        int: Maximum profit (0 if no profit possible)
    """
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit


def max_profit_one_transaction_with_days(prices: List[int]) -> tuple[int, int, int]:
    """
    Find the maximum profit and the days to buy and sell.
    Returns (max_profit, buy_day, sell_day)
    Time: O(n), Space: O(1)
    
    Args:
        prices: List of stock prices
    Returns:
        tuple: (max_profit, buy_day, sell_day)
    """
    if not prices:
        return (0, -1, -1)
    min_price = prices[0]
    min_day = 0
    max_profit = 0
    buy_day = sell_day = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            buy_day = min_day
            sell_day = i
    return (max_profit, buy_day, sell_day)


def test_max_profit_stock():
    print("=== Testing Max Profit from Stock Buy/Sell (1 Transaction) ===\n")
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 2, 3, 4, 5],
        [2, 4, 1],
        [3, 3, 5, 0, 0, 3, 1, 4],
        [],
        [1],
        [2, 1],
    ]
    for prices in test_cases:
        profit = max_profit_one_transaction(prices)
        profit_days = max_profit_one_transaction_with_days(prices)
        print(f"Prices: {prices}")
        print(f"  Max profit: {profit}")
        print(f"  (profit, buy_day, sell_day): {profit_days}")
        print()


if __name__ == "__main__":
    test_max_profit_stock()
