from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        b = []
        for i in range(n+1):
            b.append(i)
        for i in range(n+1):
            if b[i] not in nums:
                return b[i]


# ✅ Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3,0,1]))  # Expected 2
    print(s.missingNumber([0,1]))  # Expected 2
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))  # Expected 8
