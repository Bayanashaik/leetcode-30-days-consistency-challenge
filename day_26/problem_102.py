# Problem 102: Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])


# ✅ Test Cases
s = Solution()
print(s.lengthOfLastWord("Hello World"))       # 5
print(s.lengthOfLastWord("   fly me   to   the moon  "))  # 4
print(s.lengthOfLastWord("a"))                 # 1
