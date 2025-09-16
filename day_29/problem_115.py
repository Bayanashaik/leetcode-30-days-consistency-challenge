# Problem 115: Kth Missing Positive Number
# https://leetcode.com/problems/kth-missing-positive-number/

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arrr = []
        m = 2000
        for i in range(1, m+1):
            if i not in arr:
                arrr.append(i)
        return arrr[k-1]


# ✅ Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.findKthPositive([2, 3, 4, 7, 11], 5))  # Expected 9
    print(s.findKthPositive([1, 2, 3, 4], 2))      # Expected 6
