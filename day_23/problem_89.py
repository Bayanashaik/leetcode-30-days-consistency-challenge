# Problem 89: Convert Integer to the Sum of Two No-Zero Integers
# Link: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n - i):
                return [i, n - i]
        return []


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.getNoZeroIntegers(2))   # Expected: [1,1]
    print(sol.getNoZeroIntegers(11))  # Expected: [2,9] or any valid pair
    print(sol.getNoZeroIntegers(101)) # Expected: e.g. [2,99]
