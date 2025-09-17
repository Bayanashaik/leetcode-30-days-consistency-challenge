# https://leetcode.com/problems/add-digits/
# Problem 117 - Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.addDigits(38))   # Expected 2
    print(sol.addDigits(0))    # Expected 0
    print(sol.addDigits(18))   # Expected 9
    print(sol.addDigits(7))    # Expected 7
