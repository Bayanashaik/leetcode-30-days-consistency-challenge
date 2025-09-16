# Problem 114: Count of Matches in Tournament
# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        tm = 0
        while n > 1:
            if n % 2 == 0:
                tm += n // 2
                n = n // 2
            else:
                tm += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return tm


# ✅ Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.numberOfMatches(7))   # Expected 6
    print(s.numberOfMatches(14))  # Expected 13
