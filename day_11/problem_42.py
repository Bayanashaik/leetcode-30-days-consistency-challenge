# Problem 42: Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        k = sorted(list(set(nums1)))
        l = sorted(list(set(nums2)))
        for i in k:
            for j in l:
                if i == j:
                    res.append(i)
        return res


# ---------- Test Cases ----------
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([1,2,2,1], [2,2]))        # [2]
    print(sol.intersection([4,9,5], [9,4,9,8,4]))    # [4,9]
    print(sol.intersection([], [1,2]))               # []
    print(sol.intersection([1,2,3], [4,5,6]))        # []
    print(sol.intersection([1,1,1], [1,1]))          # [1]
