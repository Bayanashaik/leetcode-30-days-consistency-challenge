# Problem 81: Find Most Frequent Vowel and Consonant
# Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        d = {'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0}
        c = {}
        for i in s:
            if i in d:
                d[i] += 1
            elif i in c:
                c[i] += 1
            else:
                c[i] = 1
        max_v = 0
        for i in d.values():
            max_v = max(max_v, i)
        max_c = 0
        for j in c.values():
            max_c = max(max_c, j)
        return max_v + max_c


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxFreqSum("abac"))      # Expected: 3 (a:2 + b:1)
    print(sol.maxFreqSum("leetcode"))  # Expected: 3 (e:3 + l:1)
    print(sol.maxFreqSum("zzzz"))      # Expected: 4 (z:4 + vowels:0)
