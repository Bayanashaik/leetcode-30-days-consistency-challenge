# Problem 85: Valid Word
# Link: https://leetcode.com/problems/valid-word/

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        c = 0
        v = 0
        for i in word:
            if i.isalpha():
                if i in vowels:
                    c += 1
                else:
                    v += 1
        if len(word) >= 3 and word.isalnum() and c >= 1 and v >= 1:
            return True
        else: 
            return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("abc"))      # Expected: True
    print(sol.isValid("ab"))       # Expected: False (length < 3)
    print(sol.isValid("123"))      # Expected: False (no vowels/consonants)
    print(sol.isValid("a1c"))      # Expected: True
