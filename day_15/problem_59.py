# Problem 59: Concatenation of Array
# Link: https://leetcode.com/problems/concatenation-of-array/description/

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:] + nums[:]
        return ans


# Test Cases
s = Solution()
print(s.getConcatenation([1, 2, 1]))    # [1, 2, 1, 1, 2, 1]
print(s.getConcatenation([1, 3, 2, 1])) # [1, 3, 2, 1, 1, 3, 2, 1]
