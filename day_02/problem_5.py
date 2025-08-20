# Problem 5: Two Sum
# Link: https://leetcode.com/problems/two-sum/description/
# Approach: Use two nested loops to check every pair and return indices when their sum matches target
# Key learning: Understand brute-force approach before optimizing with hash map

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
