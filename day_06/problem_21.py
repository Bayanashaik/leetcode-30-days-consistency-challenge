# Problem: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Description: Move all zeroes in the array to the end while maintaining the relative order of non-zero elements.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for j in range(index, len(nums)):
            nums[j] = 0

# Test Cases
s = Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)
print(nums)  # [1,3,12,0,0]

nums = [0,0,1]
s.moveZeroes(nums)
print(nums)  # [1,0,0]

nums = [1,2,3]
s.moveZeroes(nums)
print(nums)  # [1,2,3]

nums = [0,0,0]
s.moveZeroes(nums)
print(nums)  # [0,0,0]

nums = []
s.moveZeroes(nums)
print(nums)  # []
