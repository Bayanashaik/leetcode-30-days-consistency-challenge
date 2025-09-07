# Problem 78: Count Equal and Divisible Pairs in an Array
# Link: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l = i * j
                if nums[i] == nums[j] and l % k == 0:
                    count += 1
        return count            


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.countPairs([3,1,2,2,2,1,3], 2))  # Expected: 4
    print(sol.countPairs([1,2,3,4], 1))        # Expected: 0
    print(sol.countPairs([1,1,1,1], 1))        # Expected: 6
