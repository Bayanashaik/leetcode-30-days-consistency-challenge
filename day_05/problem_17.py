# Problem 17: Remove Element
# Link: https://leetcode.com/problems/remove-element/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index  = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

# Example Test
if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,2,3]
    val = 3
    print(sol.removeElement(nums, val))  # Output: 2
