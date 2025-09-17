# https://leetcode.com/problems/add-strings/
# Problem 118 - Add Strings

import sys

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        return str(int(num1) + int(num2))


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.addStrings("11", "123"))   # Expected "134"
    print(sol.addStrings("456", "77"))   # Expected "533"
    print(sol.addStrings("0", "0"))      # Expected "0"
