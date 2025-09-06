# Problem 73: Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d  = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        e = {}
        for j in t:
            if j in e:
                e[j] += 1
            else:
                e[j] = 1
        for k in d:
            if k not in e or d[k] != e[k]:
                return False
        return True


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
    print(sol.isAnagram("a", "a"))              # True
    print(sol.isAnagram("abc", "cba"))          # True
