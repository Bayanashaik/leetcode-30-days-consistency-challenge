# https://leetcode.com/problems/minimum-time-visiting-all-points/
# Problem 120 - Minimum Time Visiting All Points

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            f = points[i]
            n = points[i + 1]
            res += max(abs(n[0] - f[0]), abs(n[1] - f[1]))
        return res


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])) # Expected 7
    print(sol.minTimeToVisitAllPoints([[3,2],[-2,2]]))       # Expected 5
    print(sol.minTimeToVisitAllPoints([[0,0],[2,2]]))        # Expected 2
