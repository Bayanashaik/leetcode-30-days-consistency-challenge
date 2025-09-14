# Problem 106: Maximum Ice Cream Bars
# Link: https://leetcode.com/problems/maximum-ice-cream-bars/

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for i in costs:
            if i <= coins:
                coins -= i
                count += 1
            else:
                break
        return count


# ---------- Test Cases ----------
s = Solution()
print(s.maxIceCream([1,3,2,4,1], 7))  # Expected 4
print(s.maxIceCream([10,6,8,7,7,8], 5))  # Expected 0
print(s.maxIceCream([1,6,3,1,2,5], 20))  # Expected 6
