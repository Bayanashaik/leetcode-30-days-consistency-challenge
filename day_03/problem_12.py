# Problem 12: Single Number
# Link: https://leetcode.com/problems/single-number/description/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        for key, value in d.items():
            if value == 1:
                return key


# Example test cases
print(Solution().singleNumber([2, 2, 1]))      # 1
print(Solution().singleNumber([4, 1, 2, 1, 2])) # 4
