# Problem 88: Maximum Difference Between Even and Odd Frequency I
# Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution:
    def maxDifference(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
       
        max_e = float('-inf')
        max_o = float('inf')
        for i in d.values():
            if i % 2 == 1:
                max_e = max(max_e, i)
            else: 
                max_o = min(max_o, i)
        return max_e - max_o


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDifference("aabbcc"))   # Expected: 1 (odd=3, even=2 → 3-2=1)
    print(sol.maxDifference("abc"))      # Expected: 1 (odd=1, even=0 → careful case)
    print(sol.maxDifference("zzzz"))     # Expected: -inf - 4 (edge case with no odd)
