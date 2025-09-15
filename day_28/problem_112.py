# Problem 112: Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if not nums:
            return 0
        longest = 1
        count = 1
        for i in range(len(nums)):
            if (nums[i] - nums[i-1]) == 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 1
        return longest


# ---------- Test Cases ----------
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))   # Expected 4
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Expected 9
print(s.longestConsecutive([]))   # Expected 0
