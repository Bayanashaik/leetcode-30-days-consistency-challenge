# Problem 90: Reverse Vowels of a String
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        vowel = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']
        while i < j:
            if s[i] not in vowel:
                i += 1
            elif s[j] not in vowel:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseVowels("hello"))     # Expected: "holle"
    print(sol.reverseVowels("leetcode"))  # Expected: "leotcede"
    print(sol.reverseVowels("aA"))        # Expected: "Aa"
