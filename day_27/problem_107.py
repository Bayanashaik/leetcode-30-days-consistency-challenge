# Problem 107: Sort Characters By Frequency
# Link: https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for key, val in d:
            res += key * val
        return res


# ---------- Test Cases ----------
s = Solution()
print(s.frequencySort("tree"))     # Expected "eert" or "eetr"
print(s.frequencySort("cccaaa"))   # Expected "cccaaa" or "aaaccc"
print(s.frequencySort("Aabb"))     # Expected "bbAa" or "bbaA"
