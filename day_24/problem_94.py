# Problem 94: To Lower Case
# Link: https://leetcode.com/problems/to-lower-case/

class Solution: 
    def toLowerCase(self, s: str) -> str:
        re = ""
        for i in s:
            if i.isupper():
                re += i.lower()
            else:
                re += i
        return re


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.toLowerCase("Hello"))   # Expected: "hello"
    print(sol.toLowerCase("LOVELY"))  # Expected: "lovely"
    print(sol.toLowerCase("aBc123"))  # Expected: "abc123"
