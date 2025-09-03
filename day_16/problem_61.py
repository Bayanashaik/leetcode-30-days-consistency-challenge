# Problem 61: Smallest Index With Equal Value
# Link: https://leetcode.com/problems/smallest-index-with-equal-value/description/

from typing import List

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        min_v = float('inf')
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                min_v = min(min_v, i)
        if min_v == float('inf'):
            return -1
        return min_v


# Test Cases
s = Solution()
print(s.smallestEqual([0,1,2]))          # 0
print(s.smallestEqual([4,3,2,1]))        # 2
print(s.smallestEqual([1,2,3,4,5,6,7,8]))# -1
