# Problem Link: https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/
# Description: Find max number of operations where each operation 
# takes two elements with the same sum as the first pair.

from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        res = nums[0] + nums[1]
        if len(nums) < 2:
            return 0
        count = 1
        for i in range(2, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] == res:
                count += 1
            else:
                break
        return count


# ---------- Test Cases ----------
s = Solution()
print(s.maxOperations([3,2,3,2,3,2]))   # Expected 3
print(s.maxOperations([1,1,2,2,3,3]))   # Expected 2
