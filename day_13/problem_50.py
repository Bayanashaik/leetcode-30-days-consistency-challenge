# Problem 50: Find the Distance Value Between Two Arrays
# Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in range(len(arr1)):
            vall = True
            for j in range(len(arr2)):
                d1 = abs(arr1[i] - arr2[j])
                if d1 <= d:
                    vall = False
                    break
            if vall:
                count += 1
        return count


# ---------- Test Cases ----------
if __name__ == "__main__":
    s = Solution()
    print(s.findTheDistanceValue([4,5,8], [10,9,1,8], 2))  # Expected: 2
    print(s.findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3))  # Expected: 2
    print(s.findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6))  # Expected: 1
