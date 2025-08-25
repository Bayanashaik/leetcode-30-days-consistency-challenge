# Problem Link: https://leetcode.com/problems/split-the-array/
# Description: Check if it's possible to split array into 2 groups 
# such that no number appears more than twice.

from typing import List

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        for i in d.values():
            if i > 2:
                return False
        return True


# ---------- Test Cases ----------
s = Solution()
print(s.isPossibleToSplit([1,1,2,2,3,3]))  # Expected True
print(s.isPossibleToSplit([1,2,3,4]))      # Expected True
print(s.isPossibleToSplit([1,1,1,2,2,3]))  # Expected False
