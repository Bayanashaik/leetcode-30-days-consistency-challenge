# Problem 16: Plus One
# Link: https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:   # no carry needed
                digits[i] += 1
                return digits
            digits[i] = 0       # carry over
            i -= 1
        return [1] + digits     # case like [9,9] → [1,0,0]


# Example test
s = Solution()
print(s.plusOne([1,2,3]))   # Output: [1,2,4]
print(s.plusOne([9,9,9]))   # Output: [1,0,0,0]
