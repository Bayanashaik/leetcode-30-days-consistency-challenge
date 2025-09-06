# Problem 76: Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d :
                d[i] += 1
            else:
                d[i] = 1
        res = 0
        o = False
        for i in d:
            if d[i]%2 == 0:
                res += d[i]
            else:
                res += d[i]-1
                o = True
        if o:
            res += 1
        return res


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abccccdd"))  # 7
    print(sol.longestPalindrome("a"))         # 1
    print(sol.longestPalindrome("bb"))        # 2
    print(sol.longestPalindrome("abc"))       # 1
