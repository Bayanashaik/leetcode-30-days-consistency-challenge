# Problem 64: Keep Multiplying Found Values by Two
# Link: https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/

from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original *= 2
        return original


# Test Cases
s = Solution()
print(s.findFinalValue([5,3,6,1,12], 3))  # 24
print(s.findFinalValue([2,7,9], 4))       # 4
print(s.findFinalValue([1,2,3,4,8], 2))   # 16
