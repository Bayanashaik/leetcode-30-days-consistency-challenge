# Problem 67: Next Greater Element I
# Link: https://leetcode.com/problems/next-greater-element-i/

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    nex = -1
                    for k in range(j+1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            nex = nums2[k]
                            break
                    ans.append(nex)
                    break
        return ans


# ---------- Test Cases ----------
if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement([4,1,2],[1,3,4,2]))   # [-1,3,-1]
    print(s.nextGreaterElement([2,4],[1,2,3,4]))     # [3,-1]
    print(s.nextGreaterElement([1,3,5],[6,5,4,3,2,1,7])) # [7,7,7]
