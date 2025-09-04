# Problem 68: Check If It Is a Straight Line
# Link: https://leetcode.com/problems/check-if-it-is-a-straight-line/

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates:
            if (x1-x0) * (y-y1) != (x-x1) * (y1-y0):
                return False
        return True


# ---------- Test Cases ----------
if __name__ == "__main__":
    s = Solution()
    print(s.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6]]))  # True
    print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5]]))        # False
    print(s.checkStraightLine([[0,0],[0,1],[0,2],[0,3]]))        # True
