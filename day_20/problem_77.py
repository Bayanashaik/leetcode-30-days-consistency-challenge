# Problem 77: Find N Unique Integers Sum up to Zero
# Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, (n//2)+1):
            res.append(i)
        ress = []
        for j in res:
            ress.append(-j)
        res = res[:] + ress[:]

        if len(res) < n:
            res.append(0)
        return res    


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.sumZero(5))  # Example output: [1,2,0,-1,-2]
    print(sol.sumZero(4))  # Example output: [1,2,-1,-2]
    print(sol.sumZero(1))  # Example output: [0]
