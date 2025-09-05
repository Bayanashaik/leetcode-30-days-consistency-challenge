# Problem 71: Largest Number
# Link: https://leetcode.com/problems/largest-number/

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = []
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            n.append(nums[i])
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if n[i] + n[j] < n[j] + n[i]:
                    n[i], n[j] = n[j], n[i]
        res = ""
        for i in n:
            res += i
        return "0" if res[0] == "0" else res


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([10,2]))  # "210"
    print(s.largestNumber([3,30,34,5,9]))  # "9534330"
    print(s.largestNumber([0,0]))  # "0"
