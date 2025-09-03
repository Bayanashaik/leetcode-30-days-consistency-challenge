# Problem 63: Find First Palindromic String in the Array
# Link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i[::-1] == i:
                return i
        return ""


# Test Cases
s = Solution()
print(s.firstPalindrome(["abc","car","ada","racecar","cool"])) # "ada"
print(s.firstPalindrome(["not","a","palindrome"]))             # "a"
print(s.firstPalindrome(["def","ghi"]))                        # ""
