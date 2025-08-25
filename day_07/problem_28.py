# Problem Link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/
# Description: Count how many elements are smaller than threshold k.

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] < k:
                count += 1
        return count


# ---------- Test Cases ----------
s = Solution()
print(s.minOperations([2,11,10,1,3], 10))  # Expected 3
print(s.minOperations([1,2,3], 4))         # Expected 3
print(s.minOperations([5,6,7], 5))         # Expected 0
