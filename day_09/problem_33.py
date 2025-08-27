from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            arr.append(count)
        return arr


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    s = Solution()
    print(s.smallerNumbersThanCurrent([8,1,2,2,3]))   # [4,0,1,1,3]
    print(s.smallerNumbersThanCurrent([6,5,4,8]))     # [2,1,0,3]
    print(s.smallerNumbersThanCurrent([7,7,7,7]))     # [0,0,0,0]
