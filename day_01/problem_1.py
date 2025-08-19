# Problem 1: Score of a String
# LeetCode Link: https://leetcode.com/problems/score-of-a-string/description/

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            diff = ord(s[i])-ord(s[i+1])
            if diff < 0:
                diff = -diff
            score += diff
        return score

# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.scoreOfString("hello"))  # Expected output: 13
