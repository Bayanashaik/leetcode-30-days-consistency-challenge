# Problem 51: Minimum Value to Get Positive Step by Step Sum
# Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum = 0
        ans = 0
        for e in nums:
            sum += e
            ans = min(ans, sum)
        return -ans + 1


# ---------- Test Cases ----------
if __name__ == "__main__":
    s = Solution()
    print(s.minStartValue([-3,2,-3,4,2]))  # Expected: 5
    print(s.minStartValue([1,2]))  # Expected: 1
    print(s.minStartValue([1,-2,-3]))  # Expected: 5
