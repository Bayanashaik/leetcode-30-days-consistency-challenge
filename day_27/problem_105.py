# Problem 105: H-Index
# Link: https://leetcode.com/problems/h-index/

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, n in enumerate(citations):
            if n >= i + 1:
                h = i + 1
            else:
                break
        return h


# ---------- Test Cases ----------
s = Solution()
print(s.hIndex([3,0,6,1,5]))  # Expected 3
print(s.hIndex([1,3,1]))      # Expected 1
print(s.hIndex([100]))        # Expected 1
print(s.hIndex([0,0,0]))      # Expected 0
