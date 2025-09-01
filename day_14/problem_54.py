# Problem 54: Distribute Candies
# Link: https://leetcode.com/problems/distribute-candies/

from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        k = len(set(candyType))
        res = len(candyType)//2
        if res > k:
            return k
        else: 
            return res


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.distributeCandies([1,1,2,2,3,3]))   # 3
    print(s.distributeCandies([1,1,2,3]))       # 2
    print(s.distributeCandies([6,6,6,6]))       # 1
