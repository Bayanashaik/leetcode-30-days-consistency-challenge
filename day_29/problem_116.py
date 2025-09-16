# Problem 116: Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(len(arr) - 2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False


# ✅ Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.threeConsecutiveOdds([2, 6, 4, 1]))       # Expected False
    print(s.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))  # Expected True
