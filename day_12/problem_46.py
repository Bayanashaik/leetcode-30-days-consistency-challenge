# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dis = 0
        n = len(colors)
        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                temp = i
                max_dis = max(max_dis, temp)
                break
        for i in range(n):
            if colors[i] != colors[n-1]:
                temp = n-1-i
                max_dis = max(max_dis, temp)
                break
        return max_dis


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    s = Solution()
    print(s.maxDistance([1,1,1,6,1,1,1]))  # Expected 3
    print(s.maxDistance([1,8,3,8,3]))      # Expected 4
    print(s.maxDistance([0,1]))            # Expected 1
