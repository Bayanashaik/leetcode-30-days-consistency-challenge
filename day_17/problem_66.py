# Problem 65: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/

from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        nums = str(x)
        
        if nums[0] == '-':
            res = '-' + nums[:0:-1]
        else:
            res = nums[::-1]
        reversed_num = int(res)
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num


# ---------- Test Cases ----------
if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))       # 321
    print(s.reverse(-123))      # -321
    print(s.reverse(120))       # 21
    print(s.reverse(0))         # 0
    print(s.reverse(1534236469)) # 0 (overflow)
