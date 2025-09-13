# Problem 101: Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b


# ✅ Test Cases
s = Solution()
print(s.climbStairs(2))  # 2
print(s.climbStairs(3))  # 3
print(s.climbStairs(5))  # 8
print(s.climbStairs(1))  # 1
