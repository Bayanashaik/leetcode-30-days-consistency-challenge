# Problem: Unique Number of Occurrences
# Link: https://leetcode.com/problems/unique-number-of-occurrences/description/

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d  = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        c = []
        for value in d.values():
            c.append(value)
        d = set(c)
        if len(d) != len(c):
            return False
        return True


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueOccurrences([1,2,2,1,1,3]))  # True
    print(sol.uniqueOccurrences([1,2]))          # False
    print(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # True
