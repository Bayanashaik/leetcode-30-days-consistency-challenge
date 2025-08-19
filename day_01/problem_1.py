# Problem 1: Score of a String
# LeetCode Link: https://leetcode.com/problems/score-of-a-string/description/
# Description:
# Given a string s, calculate the "score" of the string.
# The score is the sum of the absolute differences between ASCII values of adjacent characters.
# Example: For s = "hello":
#   ASCII values: h=104, e=101, l=108, l=108, o=111
#   Score = |104-101| + |101-108| + |108-108| + |108-111| = 13
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
