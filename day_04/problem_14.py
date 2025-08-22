# Problem 14: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False


# Example test
s = Solution()
print(s.containsDuplicate([1,2,3,1]))  # Output: True
print(s.containsDuplicate([1,2,3,4]))  # Output: False
