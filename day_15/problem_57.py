# Problem 57: Valid Mountain Array
# Link: https://leetcode.com/problems/valid-mountain-array/description/

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = arr.index(max(arr))
        if peak == 0 or peak == len(arr)-1:
            return False
        for i in range(peak):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(peak, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        return True


# Test Cases
s = Solution()
print(s.validMountainArray([2, 1]))            # False
print(s.validMountainArray([3, 5, 5]))         # False
print(s.validMountainArray([0, 3, 2, 1]))      # True
print(s.validMountainArray([0, 2, 3, 3, 5]))   # False
