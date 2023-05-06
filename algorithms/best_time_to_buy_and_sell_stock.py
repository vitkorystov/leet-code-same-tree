# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


p1 = [7, 1, 5, 8, 3, 6, 8, 4]


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit


res = Solution().maxProfit(p1)
print(res)  # 7
