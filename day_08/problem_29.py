# Problem: Minimum Absolute Difference
# Link: https://leetcode.com/problems/minimum-absolute-difference/description/

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_d = float('inf')
        res = []
        for i in range(len(arr)-1):
            diff = abs(arr[i+1]-arr[i])
            if diff < min_d:
                min_d = diff
                res = [[arr[i],arr[i+1]]]
            elif diff == min_d:
                res.append([arr[i],arr[i+1]])
        return res


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumAbsDifference([4,2,1,3]))     # [[1,2],[2,3],[3,4]]
    print(sol.minimumAbsDifference([1,3,6,10,15])) # [[1,3]]
    print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])) # [[-14,-10],[19,23],[23,27]]
