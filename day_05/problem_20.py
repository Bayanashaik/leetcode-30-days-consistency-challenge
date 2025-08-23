# Problem 20: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index

# Example Test
if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(nums))  # Output: 5
