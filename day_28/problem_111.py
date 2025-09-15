# Problem 111: Remove Duplicates from Sorted Array II
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        out = []
        for i in nums:
            if d[i] > 2 or d[i] == 2:
                out.append(i)
                out.append(i)
                d[i] = 0
            elif d[i] == 1:
                out.append(i)
                d[i] = 0
        for i in range(len(out)):
            nums[i] = out[i]
        return len(out)


# ---------- Test Cases ----------
s = Solution()
arr = [1,1,1,2,2,3]
k = s.removeDuplicates(arr)
print(k, arr[:k])  # Expected 5, [1,1,2,2,3]

arr = [0,0,1,1,1,1,2,3,3]
k = s.removeDuplicates(arr)
print(k, arr[:k])  # Expected 7, [0,0,1,1,2,3,3]
