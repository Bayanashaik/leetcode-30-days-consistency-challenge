# Problem 9: Check if Any Element Has Prime Frequency
# Link: https://leetcode.com/problems/check-if-any-element-has-prime-frequency/description/

from typing import List

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                d[num] = d[num] + 1
            else:
                d[num] = 1
        
        for j in d.values():
            if j < 2:
                continue
            is_prime = True
            for k in range(2, j):
                if j % k == 0:
                    is_prime = False
                    break
            if is_prime:
                return True
        return False


# Example test cases
print(Solution().checkPrimeFrequency([1, 2, 3, 2, 2]))  # True (2 occurs 3 times, 3 is prime)
print(Solution().checkPrimeFrequency([4, 4, 4, 4]))     # False
