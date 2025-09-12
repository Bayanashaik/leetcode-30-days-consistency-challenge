# Problem 98: Find the Index of the First Occurrence in a String
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i 
        return -1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))   # Expected: 0
    print(sol.strStr("leetcode", "leeto"))  # Expected: -1
    print(sol.strStr("hello", "ll"))        # Expected: 2
