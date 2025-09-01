# Problem 56: Smallest Range I
# Link: https://leetcode.com/problems/smallest-range-i/

from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        score = (max(nums)-k) - (min(nums)+k)
        if score < 0:
            return 0
        return score


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.smallestRangeI([1], 0))         # 0
    print(s.smallestRangeI([0,10], 2))      # 6
    print(s.smallestRangeI([1,3,6], 3))     # 0
