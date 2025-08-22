# Problem 13: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_pro = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_pro:
                max_pro = price - min_price
        return max_pro


# Example test
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(s.maxProfit([7,6,4,3,1]))    # Output: 0
