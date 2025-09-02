# Problem 58: Maximum Product of Two Elements in an Array
# Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


# Test Cases
s = Solution()
print(s.maxProduct([3, 4, 5, 2]))   # 12
print(s.maxProduct([1, 5, 4, 5]))   # 16
print(s.maxProduct([3, 7]))         # 12
