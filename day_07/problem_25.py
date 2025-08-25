# Problem Link: https://leetcode.com/problems/apple-redistribution-into-boxes/
# Description: Distribute apples into boxes with given capacities and 
# find the minimum number of boxes required.

from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        count = 0
        for i in range(len(apple)):
            count += apple[i]
        output = 0
        for i in capacity:
            count = count - i
            output += 1
            if count <= 0:
                break
        return output


# ---------- Test Cases ----------
s = Solution()
print(s.minimumBoxes([1,3,2], [4,3,1,5,2]))  # Expected 2
print(s.minimumBoxes([5,5,5], [2,4,6,8]))    # Expected 3
