# Problem 110: Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        if not res:
            return [-1, -1]
        return [res[0], res[-1]]


# ---------- Test Cases ----------
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))   # Expected [3, 4]
print(s.searchRange([5,7,7,8,8,10], 6))   # Expected [-1, -1]
print(s.searchRange([], 0))               # Expected [-1, -1]
