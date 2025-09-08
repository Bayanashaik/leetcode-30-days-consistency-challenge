# Problem 82: Check Balanced String
# Link: https://leetcode.com/problems/check-balanced-string/

class Solution:
    def isBalanced(self, num: str) -> bool:
        num = list((num))
        ev = 0
        for i in range(len(num)):
            if i % 2 == 0:
                ev += int(num[i])
        od = 0
        for j in range(len(num)):
            if j % 2 != 0:
                od += int(num[j])
        if ev == od:
            return True
        else:
            return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.isBalanced("1230"))   # Expected: True (1+3 = 2+0)
    print(sol.isBalanced("123"))    # Expected: False
    print(sol.isBalanced("11"))     # Expected: True
