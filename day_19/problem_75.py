# Problem 75: Find the Difference
# https://leetcode.com/problems/find-the-difference/description/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        e = {}
        for i in t:
            if i in e:
                e[i] += 1
            else:
                e[i] = 1
        for i in e:
            if i not in s or d[i] != e[i]:
                break
        return i


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))  # "e"
    print(sol.findTheDifference("", "y"))          # "y"
    print(sol.findTheDifference("a", "aa"))        # "a"
    print(sol.findTheDifference("ae", "aea"))      # "a"
