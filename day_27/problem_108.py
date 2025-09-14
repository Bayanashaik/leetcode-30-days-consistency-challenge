# Problem 108: Majority Element II
# Link: https://leetcode.com/problems/majority-element-ii/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        res = []
        for i, k in d.items():
            if k > len(nums) // 3:
                res.append(i)
        return res


# ---------- Test Cases ----------
s = Solution()
print(s.majorityElement([3,2,3]))            # Expected [3]
print(s.majorityElement([1]))                # Expected [1]
print(s.majorityElement([1,2]))              # Expected [1,2]
print(s.majorityElement([2,2,1,3]))          # Expected [2]
