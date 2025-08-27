from typing import List

class Solution: 
    def minElement(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            index = 0
            for j in str(nums[i]):
                index = index + int(j)
            arr.append(index)
        return min(arr)


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    s = Solution()
    print(s.minElement([10,12,13,14]))    # 1+0=1 (minimum)
    print(s.minElement([99,123,45]))      # 45 -> 4+5=9
    print(s.minElement([5,25,111]))       # 5 -> 5
