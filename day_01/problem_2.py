# Problem 2: Final Value of Variable After Performing Operations
# LeetCode Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
# Description:
# You are given an array of strings operations containing a list of operations.
# Each operation is either "X++", "++X", "X--", or "--X".
# Starting with X = 0, perform all the operations and return the final value of X.

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for i in range(len(operations)):
            if operations[i] == "X++" or operations[i] == "++X":
                ans += 1
            else:
                ans -= 1
        return ans

# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.finalValueAfterOperations(["--X","X++","X++"]))  # Expected output: 1
