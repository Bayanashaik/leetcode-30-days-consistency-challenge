# Problem 100: Sqrt(x)
# Link: https://leetcode.com/problems/sqrtx/

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        res = math.sqrt(x)
        ou = math.floor(res)
        return ou


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))   # Expected: 2
    print(sol.mySqrt(8))   # Expected: 2 (sqrt(8) = 2.82 -> floor = 2)
    print(sol.mySqrt(1))   # Expected: 1
    print(sol.mySqrt(0))   # Expected: 0
