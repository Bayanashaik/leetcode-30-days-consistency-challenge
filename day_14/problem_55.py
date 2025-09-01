# Problem 55: Sort Array By Parity
# Link: https://leetcode.com/problems/sort-array-by-parity/

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        return even[:] + odd[:]


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParity([3,1,2,4]))   # [2,4,3,1]
    print(s.sortArrayByParity([0]))         # [0]
    print(s.sortArrayByParity([1,3,5,7]))   # [1,3,5,7]
