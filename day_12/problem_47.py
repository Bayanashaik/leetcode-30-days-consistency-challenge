# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                return False
        return True


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(6))    # Expected True
    print(s.isUgly(1))    # Expected True
    print(s.isUgly(14))   # Expected False
