# Problem 69: Find Lucky Integer in an Array
# Link: https://leetcode.com/problems/find-lucky-integer-in-an-array/

from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        m = 0
        for k, v in d.items():
            if k == v:
                m = max(m, v)
        if not m:
            return -1
        return m


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.findLucky([2,2,3,4]))  # 2
    print(s.findLucky([1,2,2,3,3,3]))  # 3
    print(s.findLucky([5]))  # -1
