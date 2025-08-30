# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count = count + 1
        return count


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    s = Solution()
    print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))  
    # Expected 8

    print(s.countNegatives([[3,2],[1,0]]))  
    # Expected 0

    print(s.countNegatives([[1,-1],[-1,-1]]))  
    # Expected 3
