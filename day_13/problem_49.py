# Problem 49: Element Appearing More Than 25% In Sorted Array
# Link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        max_v = 0
        res = 0
        for key, value in d.items():
            if value > max_v:
                max_v = value
                res = key
        return res


# ---------- Test Cases ----------
if __name__ == "__main__":
    s = Solution()
    print(s.findSpecialInteger([1,2,2,6,6,6,6,7,10]))  # Expected: 6
    print(s.findSpecialInteger([1,1]))  # Expected: 1
