from typing import List

# Problem: Best Time to Buy and Sell Stock
# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Approach: Track minimum buy price and max profit
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
