# Problem 6: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/description/
# Approach: Convert number to string, reverse it, and compare with original
# Key learning: String reversal logic and palindrome checking

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        res = ""
        for i in range(len(s)-1, -1, -1):
            res += s[i]
        return res == s

# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))   # Output: True
    print(sol.isPalindrome(-121))  # Output: False
    print(sol.isPalindrome(10))    # Output: False
