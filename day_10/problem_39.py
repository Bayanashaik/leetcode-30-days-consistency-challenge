from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()   
        max_v = 0
        n = len(nums)
        for i in range(0, n, 2):
            for j in range(i+1, i+2):   
                min_v = min(nums[i], nums[j])
                max_v += min_v
        return max_v


# ✅ Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.arrayPairSum([1,4,3,2]))  # Expected 4
    print(s.arrayPairSum([6,2,6,5,1,2]))  # Expected 9
