# Problem 41: Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for j in range(len(nums)):
            if nums[j] in seen and j - seen[nums[j]] <= k:
                return True
            else:
                seen[nums[j]] = j
        return False


# ---------- Test Cases ----------
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))   # True
    print(sol.containsNearbyDuplicate([1,0,1,1], 1))   # True
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False
    print(sol.containsNearbyDuplicate([99, 99], 2))   # True
    print(sol.containsNearbyDuplicate([], 3))         # False
