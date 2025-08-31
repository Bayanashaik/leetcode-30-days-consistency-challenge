# Problem 52: Kids With the Greatest Number of Candies
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for i in candies:
            if i + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res


# ---------- Test Cases ----------
if __name__ == "__main__":
    s = Solution()
    print(s.kidsWithCandies([2,3,5,1,3], 3))  # Expected: [True,True,True,False,True]
    print(s.kidsWithCandies([4,2,1,1,2], 1))  # Expected: [True,False,False,False,False]
    print(s.kidsWithCandies([12,1,12], 10))   # Expected: [True,False,True]
