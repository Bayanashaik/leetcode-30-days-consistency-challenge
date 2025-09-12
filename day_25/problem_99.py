# Problem 99: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))  # Expected: 2
    print(sol.searchInsert([1,3,5,6], 2))  # Expected: 1
    print(sol.searchInsert([1,3,5,6], 7))  # Expected: 4
    print(sol.searchInsert([1,3,5,6], 0))  # Expected: 0
