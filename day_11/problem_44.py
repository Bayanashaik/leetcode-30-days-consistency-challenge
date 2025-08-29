# Problem 44: Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(abs(i*i))
        res.sort()
        return res


# ---------- Test Cases ----------
if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedSquares([-4,-1,0,3,10]))  # [0,1,9,16,100]
    print(sol.sortedSquares([-7,-3,2,3,11])) # [4,9,9,49,121]
    print(sol.sortedSquares([0]))            # [0]
    print(sol.sortedSquares([-1]))           # [1]
    print(sol.sortedSquares([1,2,3]))        # [1,4,9]
