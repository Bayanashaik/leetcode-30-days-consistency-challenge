# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_v = nums[0]
        for j in range(1, len(nums)):
            if min_v < nums[j]:
                diff = nums[j] - min_v
                max_diff = max(max_diff, diff)
            min_v = min(min_v, nums[j])
        return max_diff


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    s = Solution()
    print(s.maximumDifference([7,1,5,4]))  # Expected 4
    print(s.maximumDifference([9,4,3,2]))  # Expected -1
    print(s.maximumDifference([1,5,2,10])) # Expected 9
