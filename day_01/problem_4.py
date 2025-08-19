# Problem 4: Jewels and Stones
# LeetCode Link: https://leetcode.com/problems/jewels-and-stones/description/
# Description:
# You're given strings jewels and stones. 
# Return the number of stones that are also jewels.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for ch in stones:
            if ch in jewels:
                count += 1
        return count

# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.numJewelsInStones("aA","aAAbbbb"))  # Expected output: 3
