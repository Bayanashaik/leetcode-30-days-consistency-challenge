# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
# Problem 119 - Maximize Sum of Array After K Negations

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        nums = sorted(nums)
        if k > 0 and k % 2 != 0:
            nums[0] = -nums[0]
        res = 0
        for i in nums:
            res += i
        return res


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestSumAfterKNegations([4, 2, 3], 1))     # Expected 5
    print(sol.largestSumAfterKNegations([3, -1, 0, 2], 3)) # Expected 6
    print(sol.largestSumAfterKNegations([2, -3, -1, 5, -4], 2)) # Expected 13
