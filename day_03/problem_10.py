# Problem 10: Third Maximum Number
# Link: https://leetcode.com/problems/third-maximum-number/description/

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m = sorted(set(nums), reverse=True)  # unique + descending
        if len(m) >= 3:
            return m[2]  # third maximum
        return m[0]


# Example test cases
print(Solution().thirdMax([3, 2, 1]))       # 1
print(Solution().thirdMax([1, 2]))          # 2
print(Solution().thirdMax([2, 2, 3, 1]))    # 1
