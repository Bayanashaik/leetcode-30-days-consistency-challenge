# Problem 11: Majority Element
# Link: https://leetcode.com/problems/majority-element/description/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] = d[nums[i]] + 1
            else:
                d[nums[i]] = 1
        
        max_count = 0
        majority = None
        for key, val in d.items():
            if val > max_count:
                max_count = val
                majority = key
        return majority


# Example test cases
print(Solution().majorityElement([3, 2, 3]))       # 3
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
