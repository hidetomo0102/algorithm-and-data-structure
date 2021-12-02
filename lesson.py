# 121.Best Time to Buy and Sell Stock
from typing import List


def maxProfit(prices: List[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - prices[i - 1])
        prices[i] = min(prices[i], prices[i - 1])

    return profit
