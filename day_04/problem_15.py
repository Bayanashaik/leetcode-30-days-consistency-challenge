# Problem 15: Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)


# Example test
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s = Solution()
s.merge(nums1, 3, nums2, 3)
print(nums1)  # Output: [1,2,2,3,5,6]
