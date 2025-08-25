# Problem: Largest Number At Least Twice of Others
# Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# Description: Return the index of the largest number if it is at least twice every other number, else -1.

from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_v = max(nums)
        ind = nums.index(max_v)
        for i in nums:
            if i != max_v and max_v < 2 * i:
                return -1
        return ind

# Test Cases
s = Solution()
print(s.dominantIndex([3,6,1,0]))  # 1
print(s.dominantIndex([1,2,3,4]))  # -1
print(s.dominantIndex([0,0,3,2]))  # -1
print(s.dominantIndex([1]))        # 0
print(s.dominantIndex([0,0,0,1]))  # 3
