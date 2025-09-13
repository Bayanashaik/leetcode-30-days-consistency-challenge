# Problem 104: Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        num_set = set(nums)
        return [i for i in range(1, n + 1) if i not in num_set]


# ✅ Test Cases
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # [5,6]
print(s.findDisappearedNumbers([1,1]))  # [2]
print(s.findDisappearedNumbers([2,2]))  # [1]
