# Problem 113: Slowest Key
# https://leetcode.com/problems/slowest-key/

from typing import List

class Solution:
    def slowestKey(self, r: List[int], k: str) -> str:
        max_ = r[0]
        ind = k[0]
        for i in range(1, len(r)):
            if abs(r[i] - r[i-1]) > max_ or (abs(r[i] - r[i-1]) == max_ and k[i] > ind):
                max_ = abs(r[i] - r[i-1])
                ind = k[i]
        return ind


# ✅ Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.slowestKey([9, 29, 49, 50], "cbcd"))  # Expected "c"
    print(s.slowestKey([12, 23, 36, 46, 62], "spuda"))  # Expected "a"
