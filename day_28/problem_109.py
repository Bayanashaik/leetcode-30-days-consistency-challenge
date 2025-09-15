# Problem 109: Maximum Number of Words You Can Type
# Link: https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        n = len(text)
        count = 0
        for j in text:
            for i in j:
                if i in brokenLetters:
                    count += 1
                    break
        return n - count


# ---------- Test Cases ----------
s = Solution()
print(s.canBeTypedWords("hello world", "ad"))   # Expected 1
print(s.canBeTypedWords("leet code", "lt"))     # Expected 1
print(s.canBeTypedWords("leet code", "e"))      # Expected 0
