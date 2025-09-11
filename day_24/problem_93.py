# Problem 93: Detect Capital
# Link: https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.detectCapitalUse("USA"))      # Expected: True
    print(sol.detectCapitalUse("leetcode")) # Expected: True
    print(sol.detectCapitalUse("Google"))   # Expected: True
    print(sol.detectCapitalUse("FlaG"))     # Expected: False
