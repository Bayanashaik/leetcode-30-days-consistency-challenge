# Problem: Maximum Product of Three Numbers
# Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
# Description: Find the maximum product of any three numbers in the array.

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# Test Cases
s = Solution()
print(s.maximumProduct([1,2,3]))           # 6
print(s.maximumProduct([1,2,3,4]))         # 24
print(s.maximumProduct([-1,-2,-3]))        # -6
print(s.maximumProduct([-10,-10,5,2]))     # 500
print(s.maximumProduct([-5,-4,-3,-2,-1]))  # -6
print(s.maximumProduct([0,0,0]))           # 0
