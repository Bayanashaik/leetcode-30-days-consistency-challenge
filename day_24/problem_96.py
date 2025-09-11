# Problem 96: Find the Difference of Two Arrays
# Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0 = []
        ans1 = []
        for i in nums1:
            if i not in nums2:
                ans0.append(i)
        for i in nums2:
            if i not in nums1:
                ans1.append(i)
        ans2 = list(set(ans0))
        ans3 = list(set(ans1))
        out = [ans2, ans3]
        return out


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDifference([1,2,3], [2,4,6]))  # Expected: [[1,3],[4,6]]
    print(sol.findDifference([1,2,3,3], [1,1,2,2])) # Expected: [[3],[]]
    print(sol.findDifference([5,6], [7,8]))      # Expected: [[5,6],[7,8]]
