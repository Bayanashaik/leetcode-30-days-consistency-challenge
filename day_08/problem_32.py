# Problem: Rank Transform of an Array
# Link: https://leetcode.com/problems/rank-transform-of-an-array/description/

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        s = sorted(list(set(arr)))
        for i in range(len(s)):
            d[s[i]] = i+1
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
        return arr


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.arrayRankTransform([40,10,20,30]))       # [4,1,2,3]
    print(sol.arrayRankTransform([100,100,100]))       # [1,1,1]
    print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12])) # [5,3,4,2,8,6,7,1,3]
