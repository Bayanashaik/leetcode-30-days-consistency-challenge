# Problem 62: Find Target Indices After Sorting Array
# Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res


# Test Cases
s = Solution()
print(s.targetIndices([1,2,5,2,3], 2))   # [1, 2]
print(s.targetIndices([1,2,5,2,3], 3))   # [3]
print(s.targetIndices([1,2,5,2,3], 5))   # [4]
