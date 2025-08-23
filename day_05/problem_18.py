# Problem 18: Height Checker
# Link: https://leetcode.com/problems/height-checker/

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        output = 0
        for i in range(len(expected)):
            if heights[i] != expected[i]:
                output += 1
        return output

# Example Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.heightChecker([1,1,4,2,1,3]))  # Output: 3
