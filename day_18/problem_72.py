# Problem 72: Largest Odd Number in String
# Link: https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.largestOddNumber("52"))  # "5"
    print(s.largestOddNumber("4206"))  # ""
    print(s.largestOddNumber("35427"))  # "35427"
