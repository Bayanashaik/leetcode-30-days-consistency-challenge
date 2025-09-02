# Problem 60: Count Number of Pairs With Absolute Difference K
# Link: https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/

from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count


# Test Cases
s = Solution()
print(s.countKDifference([1, 2, 2, 1], 1))   # 4
print(s.countKDifference([1, 3], 3))         # 0
print(s.countKDifference([3, 2, 1, 5, 4], 2))# 3
