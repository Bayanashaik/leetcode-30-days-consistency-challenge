# Problem: Find Numbers with Even Number of Digits
# Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for i in nums:
            if len(str(i))%2==0:
                even += 1
        return even


# -------------------- Test Cases --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.findNumbers([12,345,2,6,7896])) # 2
    print(sol.findNumbers([555,901,482,1771])) # 1
    print(sol.findNumbers([1,22,333,4444,55555])) # 2
