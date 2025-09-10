# Problem 91: First Unique Character in a String
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i, j in d.items():
            if j == 1:
                return s.index(i)
                break
        return -1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))     # Expected: 0
    print(sol.firstUniqChar("loveleetcode")) # Expected: 2
    print(sol.firstUniqChar("aabb"))         # Expected: -1
